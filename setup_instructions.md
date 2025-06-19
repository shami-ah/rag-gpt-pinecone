INSTRUCTIONS - How to Run the RAG Pipeline on Your PC

1. Open Git Bash / Terminal and clone the GitHub repository:
   git clone https://github.com/Shami4004/rag-gpt-pinecone.git

2. Navigate into the folder:
   cd rag-gpt-pinecone

3. Set up the virtual environment:
   python -m venv env

4. Activate the environment:
   - For Windows: env\Scripts\activate
   - For Mac/Linux: source env/bin/activate

5. Install all required packages:
   pip install -r requirements.txt

6. Add your API keys in a `.env` file in the root folder:
   OPENAI_API_KEY=your_openai_key
   PINECONE_API_KEY=your_pinecone_key
   PINECONE_ENV=your_pinecone_environment_id

7. Add a test document in: `data/sample.txt`

8. Run the RAG pipeline:
   python src/rag_pipeline.py

If you need support with environment setup, please let me know.