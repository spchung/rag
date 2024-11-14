from api.src.milvus.db import client
from llama_index.readers.file import PyMuPDFReader
from llama_index.core.schema import MetadataMode
from sentence_transformers import SentenceTransformer
from llama_index.core.node_parser import SentenceSplitter

loader = PyMuPDFReader()
documents = loader.load(file_path="docs/example.pdf")

text_splitter = SentenceSplitter(
  chunk_size=512,          # Maximum characters per chunk
  chunk_overlap=50,        # Number of characters to overlap between chunks
  separator=" ",           # Split on spaces to avoid breaking words
  paragraph_separator="\n\n",
  secondary_chunking_regex="[^,.;]+[,.;]?"  # Splits on sentence boundaries
)

nodes = text_splitter.get_nodes_from_documents(documents)

def process_text(text):
  text = text.replace("\n", "")
  return text
  

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

data = [
  {"id": i, "node_id": node_ids[i], "vector": embeddings[i], "text": sentences[i]} for i in range(len(embeddings))
]

res = client.insert(collection_name="raggyhuggin", data=data)
