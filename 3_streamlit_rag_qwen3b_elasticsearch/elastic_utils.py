# Query and retrieve from elasticsearch

from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
es = Elasticsearch("http://localhost:9200")

print(es.info())

def search(query, top_k=3):
    query_vector = model.encode(query).tolist()
    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                "params": {"query_vector": query_vector}
            }
        }
    }
    response = es.search(index="docs-index", body={
        "size": top_k,
        "query": script_query
    })

    return [hit['_source']['content'] for hit in response['hits']['hits']]
