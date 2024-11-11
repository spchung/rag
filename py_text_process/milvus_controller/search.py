from sentence_transformers import SentenceTransformer
from llama_index.core.schema import MetadataMode
from db import client

from pymilvus import model
# embedding_fn = model.DefaultEmbeddingFunction()

# query_vectors = embedding_fn.encode_queries(["What is the capital of France?"])

# res = client.search(s
#     collection_name="raggy",  # target collection
#     data=query_vectors,  # query vectors
#     limit=1,  # number of returned entities
#     output_fields=["text"],  # specifies fields to be returned
# )

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
query_vectors = model.encode(["what is Passive Clustering"])

res = client.search(
    collection_name="raggyhuggin",  # target collection
    data=query_vectors,  # query vectors
    limit=1,  # number of returned entities
    output_fields=["text"],  # specifies fields to be returned
)



import json
res = res[0]

for entity in res:
  print(entity['entity']['text'])


