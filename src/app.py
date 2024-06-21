import uuid

from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from helpers.document_loader import get_db
from helpers.chat_history import get_memory

load_dotenv()

# Embeddings are loaded from the Milvus collection, db
db = get_db()

# generate base chat model, OLLAMA has to be run with the model llama3
llm = ChatOllama(model="llama3")

##### HISTORY AWARE CHAIN SETUP #####
contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

history_aware_retriever = create_history_aware_retriever(
    llm, db.as_retriever(), contextualize_q_prompt
)

##### QUESTION ANSWERING CHAIN SETUP #####
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)


##### RAG CHAIN SETUP #####
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_memory,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)


#### Interaction ####
conversation_session_id = str(uuid.uuid4())
if (
    session_id := input(
        "Enter session ID if you want to continue the conversation, or press Enter to start a new conversation: "
    )
) != "":
    conversation_session_id = session_id
##### CHAT LOOP #####
while True:
    query = input("You: ")
    if query == "q":
        break
    output = conversational_rag_chain.invoke(
        {"input": query},
        config={"configurable": {"session_id": conversation_session_id}},
    )["answer"]
    print(f"User: {query}")
    print(f"Bot: {output}")
