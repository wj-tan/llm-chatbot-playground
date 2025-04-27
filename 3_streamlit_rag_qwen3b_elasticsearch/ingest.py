# Ingest and index documents into elasticsearch

from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import os
import uuid

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")

INDEX_NAME = "docs-index"

def create_index():
    #if es.exists(index=INDEX_NAME):
    es.delete(index=INDEX_NAME)
    es.create(index=INDEX_NAME, body={
        "mappings": {
            "properties": {
                "content": {"type": "text"},
                "embedding": {"type": "dense_vector", "dims": 384, "index": True, "similarity": "cosine"}
            }
        }
    })

def index_docs(folder_path):
    docs = []
    for filename in os.listdir(folder_path):
        with open(os.path.join(folder_path, filename), "r") as f:
            text = f.read()
            chunks = text.split("\n\n")  # crude chunking
            for chunk in chunks:
                embedding = model.encode(chunk).tolist()
                docs.append({
                    "_index": INDEX_NAME,
                    "_id": str(uuid.uuid4()),
                    "_source": {
                        "content": chunk,
                        "embedding": embedding
                    }
                })
    bulk(es, docs)

if __name__ == "__main__":
    create_index()
    index_docs("sample_docs")
