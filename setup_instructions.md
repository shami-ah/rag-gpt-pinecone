Windows Setup Instructions for RAG Pipeline

Follow these instructions to set up the Retrieval-Augmented Generation (RAG) pipeline on Windows.
	1.	Install Requirements:

	•	Python 3.9+ from https://www.python.org
	•	Git from https://git-scm.com/download/win
	•	Get your API keys:
	•	OpenAI: https://platform.openai.com/account/api-keys
	•	Pinecone: https://app.pinecone.io/

	2.	Clone the Project:
Open Command Prompt or PowerShell:
git clone https://github.com/your-org/rag-gpt-pinecone.git
cd rag-gpt-pinecone
	3.	Create and Activate Virtual Environment:
python -m venv env
.\env\Scripts\activate
	4.	Install Dependencies:
pip install -r requirements.txt
	5.  Rename .env.example to .env
	6.	Replace your-openai-api-key-here and your-pinecone-api-key-here with your actual API keys.

Note: If you face errors like “Pinecone not found”, do this:
pip uninstall pinecone-client
pip install pinecone
	5.	Configure .env File:
Rename .env.example to .env
Edit .env and add your keys:
OPENAI_API_KEY=sk-xxxxx
PINECONE_API_KEY=your-pinecone-key
	6.	Update Sample Text:
Edit the raw_text in rag_pipeline.py or use your own file.
	7.	Run the Script:
python src/rag_pipeline.py

Common Issues:
	•	Pinecone ImportError:
Uninstall old client:
pip uninstall pinecone-client
Install the new one:
pip install pinecone
	•	ChatOpenAI Warning:
Update LangChain-OpenAI:
pip install -U langchain-openai

Support:
Muhammad Ahtesham Ahmad
Email: iamshami1996@gmail.com