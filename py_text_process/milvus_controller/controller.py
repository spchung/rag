
from milvus_controller.milvus_connect import MilvusConnector

class MilvusController:
  def __init__ (self, host, port):
    self.client = MilvusConnector(uri=host, token=port).connect()
  
  def create_collection(self, collection_name, ) -> bool:
    self.client.create_collection(collection_name, )
    return True
  
  def drop_collection(self, collection_name):
    self.client.drop_collection(collection_name)
    return True
  
  def query(self, collection_name, vector, top_k):
    return self.client.search(collection_name, vector, top_k)
  

class MilvusCollectionHelper:
  def __init__(self, collection_name, dimension):
    self.collection_name = collection_name
    self.dimension = dimension
  
  def insert(self, client, data):
    return client.insert(collection_name=self.collection_name, data=data)
  
  def get_collection_info(self, client):
    return client.get_collection_info(collection_name=self.collection_name)
  
  def get_collection_stats(self, client):
    return client.get_collection_stats(collection_name=self.collection_name)
  
  def count(self, client):
    return client.count_entities(collection_name=self.collection_name)
  
  def delete(self, client):
    return client.delete_entity_by_id(collection_name=self.collection_name)
  
  def search(self, client, vector, top_k):
    return client.search(collection_name=self.collection_name, vector=vector, top_k=top_k)
  
  def search_in_files(self, client, file_path, top_k):
    return client.search_in_files(collection_name=self.collection_name, file_path=file_path, top_k=top_k)
  
  def describe_index(self, client):
    return client.describe_index(collection_name=self.collection_name)
  
  def create_index(self, client, index_type, nlist):
    return client.create_index(collection_name=self.collection_name, index_type=index_type, nlist=nlist)
  
  def drop_index(self, client):
    return client.drop_index(collection_name=self.collection_name)
  
  def get_index_state(self, client):
    return client.get_index_state(collection_name=self.collection_name)
  
  def get_index_file_size(self, client):
    return client.get_index_file_size(collection_name=self.collection_name)
  
  def load_collection(self, client):
    return client.load_collection(collection_name=self.collection_name)
  
  def release_collection(self, client):
    return client.release_collection(collection_name=self.collection_name)
  
  def get_entity_by_id(self, client, ids):
    return client.get_entity_by_id(collection_name=self.collection_name, ids=ids)
  
  def list_id_in_segment(self, client, segment_id):
    return client.list_id_in_segment(collection_name=self.collection_name, segment_id=segment_id)
  
  def get_entity_info(self, client, id):
    return client.get_entity_info(collection_name=self.collection_name, id=id)
  
  def get_entity_ids(self, client):
    return client.get_entity_ids(collection_name=self.collection_name)
  
  def get_entity_count(self, client):
    return client.get_entity_count(collection_name=self.collection_name)