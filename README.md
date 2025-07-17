RAG Pipeline with GPT & Pinecone

This project demonstrates a fully functional Retrieval-Augmented Generation (RAG) pipeline using:
	•	LangChain for orchestration
	•	OpenAI GPT for natural language processing
	•	Pinecone for vector storage and fast retrieval
	•	Dotenv for secure environment variable handling

What It Does:
	•	Splits a text document into manageable chunks.
	•	Converts those chunks into embeddings using OpenAI.
	•	Stores them in a Pinecone index.
	•	Enables querying via GPT using the most relevant documents retrieved from Pinecone.

Project Structure:
rag-gpt-pinecone/
├── .env.example         –> Environment variable template
├── requirements.txt     –> Python dependencies
├── setup_instructions.md –> Detailed setup guide
├── your_file.txt        –> Sample input file
└── src/
└── rag_pipeline.py  –> Main pipeline script

# How to Use This App

1. **Install Docker Desktop**: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. **Double-click `run.bat`** file
3. Wait for it to open your browser at `http://localhost:7860`
4. Enter your **API Key**, **upload your file**, and **ask your question**
5. You’re done — no coding or command line needed!


Author:
Muhammad Ahtesham Ahmad
Engineer • Entrepreneur • AI Expert
Email: iamshami1996@gmail.com