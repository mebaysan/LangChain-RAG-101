import os

class APP_CONF:
    # App configuration
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_CHAT_HISTORY_TABLE = os.getenv("DB_CHAT_HISTORY_TABLE")
    MILVUS_HOST = os.getenv("MILVUS_HOST")
    MILVUS_PORT = os.getenv("MILVUS_PORT")
    MILVUS_COLLECTION_NAME = os.getenv("MILVUS_COLLECTION_NAME")