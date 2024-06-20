# Introduction

101 level implementation of RAG with History awareness by LangChain. I used [Effective Python: 90 Specific Ways to Write Better Python, 2nd Edition](https://www.oreilly.com/library/view/effective-python-90/9780134854717/) for my LLM. You can buy/access the book by using the link.

Technologies used are:
- **Python3.11**
- Ollama
- Milvus DB
- LangChain
- Postgres
- Docker

# Usage

You can run `init.sh` to run LLAMA-3:8B by OLLAMA and needed services as Docker containers. Obviously, you havce to have OLLAMA and Docker.

You have to have `.env` file in `src` folder. You can just rename `.env.local` file as `.env`.

You can run `src/app.py` to communicate with the LLM.

You also can enhance & improve [document_loader.py](./src/helpers/document_loader.py) to embed your own documents.

I also added a package [`experimental`](./src/experimental/) to manually test some functions.