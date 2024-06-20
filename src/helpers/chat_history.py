from langchain_postgres import PostgresChatMessageHistory
import psycopg


def get_memory(session_id: str) -> PostgresChatMessageHistory:
    """Returns a PostgresChatMessageHistory object for a session.

    Args:
        session_id (str): Session ID to get the memory for.

    Returns:
        PostgresChatMessageHistory: Memory object for the session to use in history-aware retrieval.
    """
    connection_info = "postgresql://postgres:postgres@localhost/chatbot_memory"
    sync_connection = psycopg.connect(connection_info)
    table_name = "chat_history"
    PostgresChatMessageHistory.create_tables(sync_connection, table_name)
    session_id = session_id
    memory = PostgresChatMessageHistory(
        table_name,
        session_id,
        sync_connection=sync_connection,
    )
    return memory
