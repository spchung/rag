from .db import client
from llama_index.readers.file import PyMuPDFReader
from llama_index.core.schema import MetadataMode
from sentence_transformers import SentenceTransformer
from llama_index.core.node_parser import SentenceSplitter

def process_text(text):
  text = text.replace("\n", "")
  return text

def pdf_pipeline(file_path):
  loader = PyMuPDFReader()
  documents = loader.load(file_path=file_path)

  text_splitter = SentenceSplitter(
    chunk_size=512,          # Maximum characters per chunk
    chunk_overlap=50,        # Number of characters to overlap between chunks
    separator=" ",           # Split on spaces to avoid breaking words
    paragraph_separator="\n\n",
    secondary_chunking_regex="[^,.;]+[,.;]?"  # Splits on sentence boundaries
  )

  # llama index node - represent chuck of text
  nodes = text_splitter.get_nodes_from_documents(documents)

  node_ids = [node.node_id for node in nodes]
  sentences = [process_text(node.get_text()) for node in nodes]

  model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
  embeddings = model.encode(sentences)

  if client.has_collection(collection_name="raggyhuggin"):
    client.drop_collection(collection_name="raggyhuggin")
  client.create_collection(
    collection_name="raggyhuggin",
    dimension=384, 
  )

  '''
  save seq_id, node_id, vector, text, src_doc to milvus
  '''
  data = [
    {"seq_id": i, "node_id": node_ids[i], "vector": embeddings[i], "text": sentences[i], 'src_doc': file_path} for i in range(len(embeddings))
  ]

  res = client.insert(collection_name="raggyhuggin", data=data)