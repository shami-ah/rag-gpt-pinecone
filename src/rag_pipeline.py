import os
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA

from pinecone import Pinecone, ServerlessSpec

# ========== Step 1: Load documents ==========
loader = TextLoader("data/sample.txt")
documents = loader.load()

# ========== Step 2: Split text into chunks ==========
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

# ========== Step 3: Initialize Pinecone ==========
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY") or "your-pinecone-api-key"
PINECONE_ENV = os.getenv("PINECONE_ENV") or "your-region"  # e.g., "us-west-2"

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "rag-index"
dimension = 1536
metric = "cosine"

# Create index if it doesn't exist
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric=metric,
        spec=ServerlessSpec(cloud="aws", region=PINECONE_ENV)
    )

# Connect to index
index = pc.Index(index_name)

# ========== Step 4: Embed and upload documents ==========
embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY") or "your-openai-api-key")

vectorstore = LangchainPinecone.from_documents(
    docs, embedding, index_name=index_name
)

# ========== Step 5: Setup Retrieval-QA Chain ==========
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY") or "your-openai-api-key")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

# ========== Step 6: Query interface (placeholder) ==========
query = "What is this document about?"
result = qa_chain.run(query)
print("Answer:", result)