from database.milvus.pipeline import pdf_pipeline
from sentence_transformers import SentenceTransformer
from database.milvus.db import client

pdf_pipeline("api/src/docs/example.pdf")


model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(["What is passice clustering?"])

# If you don't have the embedding function you can use a fake vector to finish the demo:
# query_vectors = [ [ random.uniform(-1, 1) for _ in range(768) ] ]

res = client.search(
  collection_name="raggyhuggin",  # target collection
  data=embeddings,  # query vectors
  limit=1,  # number of returned entities
  output_fields=["text", 'src'],  # specifies fields to be returned
)

print(res)