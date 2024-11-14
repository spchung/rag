from api.src.database.milvus.db import client
from llama_index.core.schema import Document
from llama_index.readers.file import PyMuPDFReader
from llama_index.core.schema import MetadataMode
from sentence_transformers import SentenceTransformer
from llama_index.core.node_parser import SentenceSplitter
from typing import List

def load_pdf(file_path) -> List[Document]:
  loader = PyMuPDFReader()
  documents = loader.load(file_path=file_path)
  return documents