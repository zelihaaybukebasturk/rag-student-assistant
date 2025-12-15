from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
import os

PERSIST_DIR = "../vectorstore"

def build_embeddings():
    emb = OllamaEmbeddings(model="nomic-embed-text")

    import pandas as pd
    df = pd.read_csv("../dataset.csv")

    texts = df["content"].tolist()
    metadatas = df.to_dict(orient="records")

    db = Chroma.from_texts(
        texts=texts,
        embedding=emb,
        persist_directory=PERSIST_DIR,
        metadatas=metadatas,
    )

    db.persist()
    print("Embeddings oluşturuldu ve vectorstore kaydedildi.")

if __name__ == "__main__":
    build_embeddings()
