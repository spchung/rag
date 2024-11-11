pg_db
- milvus_collections
  - id `int`
  - collection_name `varchar`
  - source_document `varchar`
  - embedding_model_id `int`
  - metadata `json`
  - tags `varchar`
- source_docs
  - id `int`
  - url `varchar`
- embedding_model
  - id `int`
  - type (HuggingFace | milvus | ... etc) `varchar`
  - name `varchar`

services:
- api
