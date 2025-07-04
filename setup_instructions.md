Windows & Docker Setup Instructions for RAG Pipeline

🚀 Overview

This guide will help you set up the Retrieval-Augmented Generation (RAG) pipeline using GPT and Pinecone on your Windows 10 PC. You can run it either via local Python or using the recommended Docker setup.

⸻

✅ Prerequisites
	1.	Python 3.9+ – Download from python.org
	2.	Git – Download from git-scm.com
	3.	Docker Desktop (if using Docker) – Download here
	4.	API Keys
	•	OpenAI: Get your API key
	•	Pinecone: Get your API key

⸻

💻 Local Python Setup (No Docker)

1. Clone the Project
git clone https://github.com/shami-ah/rag-gpt-pinecone.git
cd rag-gpt-pinecone
2. Set Up Virtual Environment
python -m venv env
.\env\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables
	•	Rename .env.template → .env
	•	Open .env and add your keys:
	 OPENAI_API_KEY=sk-xxxxxxxx
     PINECONE_API_KEY=your-pinecone-key
5. Run the RAG Pipeline
python src/rag_pipeline.py
Docker Setup (Recommended)

1. Prepare Environment Variables
	•	Copy .env.template → .env
	•	Fill in your API keys inside .env

2. Build and Run with Docker
docker-compose up --build
This will:
	•	Install dependencies inside the container
	•	Run the rag_pipeline.py script
	•	Show your query result directly in the terminal

⸻

🧪 Customizing Your Data
	•	To use your own text or dataset, modify the raw_text in src/rag_pipeline.py, or add logic to load from a file.

⸻

🧯 Troubleshooting

Pinecone Errors?
pip uninstall pinecone-client
pip install pinecone
ChatOpenAI Warnings?
pip install -U langchain-openai

Support

Muhammad Ahtesham Ahmad
✉️ iamshami1996@gmail.com