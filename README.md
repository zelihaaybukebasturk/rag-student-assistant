# RAG Student Assistant 

A Retrieval-Augmented Generation (RAG) based web application that helps students
ask questions directly from course materials (PDFs) uploaded by instructors.

This project is designed as a **student study assistant**, allowing learners
to interact with lecture notes through natural language questions.

---

## Features

-  User authentication (Register / Login)
-  Student interface for asking questions
-  Teacher-only PDF upload system
-  Automatic PDF ingestion and vectorization
-  RAG-based question answering
-  Web interface built with Flask
-  Local LLM support using Ollama (no external API required)

---

## Tech Stack

- **Python 3.9**
- **Flask**
- **LangChain**
- **ChromaDB**
- **Ollama**
  - Mistral (LLM)
  - nomic-embed-text (Embeddings)
- **SQLite** (User database)
- **HTML / CSS** (Frontend)

