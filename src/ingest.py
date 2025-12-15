import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

PERSIST_DIR = "db"

def ingest_pdf(pdf_path):
    """PDF'yi yükler, parçalar ve vektör veritabanına ekler."""
    print(f"[INFO] Loading PDF: {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    emb = OllamaEmbeddings(model="nomic-embed-text")

    db = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=emb
    )

    print("[INFO] Adding documents to vector DB…")
    db.add_documents(docs)
    db.persist()

    print("[SUCCESS] PDF başarıyla eklendi!")

    return True
