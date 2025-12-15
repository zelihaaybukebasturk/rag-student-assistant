from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PERSIST_DIR = os.path.join(BASE_DIR, "..", "vectorstore")

emb = OllamaEmbeddings(model="nomic-embed-text")

db = Chroma(persist_directory=PERSIST_DIR, embedding_function=emb)

llm = ChatOllama(model="mistral")

def ask_question(question):
    docs = db.similarity_search(question, k=4)
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
Aşağıdaki bağlama göre soruyu kısa, net ve anlaşılır şekilde cevapla.

Bağlam:
{context}

Soru:
{question}

Cevap:
"""

    response = llm.invoke(prompt)
    return response.content

# if __name__ == "__main__": kısmı artık yok
