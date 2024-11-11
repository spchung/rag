
from milvus_controller.milvus_connect import MilvusConnector

class MilvusController:
  def __init__ (self, host, port):
    self.client = MilvusConnector(uri=host, token=port).connect()
  
  def create_collection(self, collection_name, dimension):
    self.client.create_collection(collection_name, dimension)