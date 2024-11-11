# 1 load document
from db import client
from llama_index.readers.file import PyMuPDFReader
from llama_index.core.schema import MetadataMode

loader = PyMuPDFReader()
documents = loader.load(file_path="docs/example.pdf")

# split into nodes
from llama_index.core.node_parser import SentenceSplitter

text_splitter = SentenceSplitter(
  chunk_size=512,          # Maximum characters per chunk
  chunk_overlap=50,        # Number of characters to overlap between chunks
  separator=" ",           # Split on spaces to avoid breaking words
  paragraph_separator="\n\n",
  secondary_chunking_regex="[^,.;]+[,.;]?"  # Splits on sentence boundaries
)

nodes = text_splitter.get_nodes_from_documents(documents)

# run embedding model
from pymilvus import model
embedding_fn = model.DefaultEmbeddingFunction()
docs = [node.get_content(metadata_mode=MetadataMode.EMBED) for node in nodes]

vectors = embedding_fn.encode_documents(docs)

# store in milvus
if client.has_collection(collection_name="raggy"):
    client.drop_collection(collection_name="raggy")
client.create_collection(
  collection_name="raggy",
  dimension=768,  # The vectors we will use in this demo has 768 dimensions
)

data = [
  {"id": i, "vector": vectors[i], "text": docs[i]} for i in range(len(vectors))
]

res = client.insert(collection_name="raggy", data=data)