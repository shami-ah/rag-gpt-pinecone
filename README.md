# RAG-GPT-Pinecone

This project uses LangChain, OpenAI, and Pinecone to build a Retrieval-Augmented Generation (RAG) pipeline from `.txt` files.

---

## 🧠 Features

- Upload any `.txt` file
- Converts text into embeddings using OpenAI
- Stores vectors in Pinecone
- Asks questions and retrieves answers using LangChain's `RetrievalQA`

---

## 📁 Project Structure
rag-gpt-pinecone/
├── data/                 # Folder for .txt input files
│   └── sample.txt
├── src/
│   ├── init.py
│   └── rag_pipeline.py   # Main script
├── .gitignore
├── requirements.txt
├── .env.template
└── README.md

---

## 🛠 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/rag-gpt-pinecone.git
cd rag-gpt-pinecone