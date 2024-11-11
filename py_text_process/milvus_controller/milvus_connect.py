from pymilvus import MilvusClient
client = MilvusClient(uri="http://localhost:19530", token="root:Milvus")


client = None

class MilvusConnector:
  def __init__(self, uri, token):
    self.client = client
    self.uri = uri
    self.token = token
  
  def connect(self):
    try:
      if self.client is None:
        self.client = MilvusClient(uri=self.uri, token=self.token)
      return self.client
    except Exception as e:
      raise e