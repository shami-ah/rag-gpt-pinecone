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

Quick Start:
	1.	Clone the Repository:
git clone https://github.com/your-org/rag-gpt-pinecone.git
cd rag-gpt-pinecone
	2.	Create a Virtual Environment:
python -m venv env
source env/bin/activate  (or env\Scripts\activate on Windows)
	3.	Install Dependencies:
pip install -r requirements.txt
	4.	Configure Environment:
Rename .env.example to .env and add:
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
	5.	Add Your Text:
Edit the raw_text section in rag_pipeline.py or load your file.
	6.	Run the Pipeline:
python src/rag_pipeline.py

Expected Output Example:
✅ Successfully added documents to Pinecone using new API.
📄 Query Result:
The sample text is about LangChain enabling retrieval-augmented generation (RAG) with Pinecone, which is useful for LLM-powered apps.

Author:
Muhammad Ahtesham Ahmad
Engineer • Entrepreneur • AI Expert
Email: iamshami1996@gmail.com