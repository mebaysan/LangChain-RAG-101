from langchain_milvus.vectorstores import Milvus
from langchain_community.embeddings import OllamaEmbeddings

URI = "tcp://localhost:19530"
COLLECTION_NAME = "baysan_demo"
EMBEDDING_MODEL = OllamaEmbeddings(model="llama3")


def get_db() -> Milvus:
    """Get Milvus object with the connection to the Milvus collection.

    Returns:
        Milvus: Milvus object with the connection to the Milvus collection.
    """
    return Milvus(
        EMBEDDING_MODEL, connection_args={"uri": URI}, collection_name=COLLECTION_NAME
    )


db = get_db()
# GET FIRST 5 SIMILAR DOCUMENTS TO THE QUERY
res = db.search("walrus operator", "similarity", top_k=3)
print(res)
