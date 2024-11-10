from pymilvus import model
from pymilvus import MilvusClient

embedding_fn = model.DefaultEmbeddingFunction()

client = MilvusClient(uri="http://localhost:19530", token="root:Milvus")