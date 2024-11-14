from src.milvus.db import client
from typing import List
from nltk import sent_tokenize
from pprint import pprint
import pymupdf4llm

# md_text = pymupdf4llm.to_markdown("docs/example.pdf")
# print(md_text)

# pdf_path = "docs/example.pdf"

llama_reader = pymupdf4llm.LlamaMarkdownReader()
llama_docs = llama_reader.load_data("docs/example.pdf")


from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import MilvusVectorStore
from llama_index.storage.storage_context import StorageContext

# Milvus connection settings
MILVUS_HOST = "localhost"
MILVUS_PORT = 19530
COLLECTION_NAME = "your_collection_name"

# get pages as raw text
# def readPdfPages(path) -> List[str]:
#   reader = PdfReader(path)
#   number_of_pages = len(reader.pages)
#   pages = []
  
#   for i in range(number_of_pages):
#     pages.append(reader.pages[i].extract_text())
#   return pages

# pages = readPdfPages("docs/example.pdf")

# def preprocess(text: str) -> str:
#   chunks = text.replace("\n", "")
#   # sentences = []
#   # for chunk in chunks:
#   #   sentences += sent_tokenize(chunk)
#   sentences = sent_tokenize(chunks)
#   return sentences



# preprocessed = preprocess(pages[1])
# pprint(preprocessed)

# # for page in pages:
# #   print(page)
# #   print("---------------------\n")




