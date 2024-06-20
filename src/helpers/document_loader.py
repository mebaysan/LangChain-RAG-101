from langchain_milvus.vectorstores import Milvus
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from datetime import datetime

from helpers.conf import APP_CONF
from helpers.utils import wip_time

URI = f"tcp://{APP_CONF.MILVUS_HOST}:{APP_CONF.MILVUS_PORT}"
COLLECTION_NAME = APP_CONF.MILVUS_COLLECTION_NAME
EMBEDDING_MODEL = OllamaEmbeddings(model="llama3")


def prepare_documents_and_store():
    """Generate documents from a PDF file and store them in Milvus."""
    start_time = datetime.now()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    raw_documents = PyPDFLoader("./data/effective_python.pdf").load()
    documents = text_splitter.split_documents(raw_documents)

    db = Milvus.from_documents(
        documents,
        EMBEDDING_MODEL,
        connection_args={"uri": URI},
        collection_name=COLLECTION_NAME,
    )
    print(f"Documents are stored in Milvus: {URI} in collection {COLLECTION_NAME}")
    wip_time(start_time)


def get_db() -> Milvus:
    """Get Milvus object with the connection to the Milvus collection.

    Returns:
        Milvus: Milvus object with the connection to the Milvus collection.
    """
    return Milvus(
        EMBEDDING_MODEL, connection_args={"uri": URI}, collection_name=COLLECTION_NAME
    )


if __name__ == "__main__":
    print("Script started to prepare documents and store in Milvus.")
    prepare_documents_and_store()
