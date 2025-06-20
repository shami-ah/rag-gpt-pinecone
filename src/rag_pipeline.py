import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from pinecone import Pinecone, ServerlessSpec
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI  # ✅ correct import

# Load .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = "rag-index"
NAMESPACE = "default"

# Init Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create index if not exists
if INDEX_NAME not in [i.name for i in pc.list_indexes()]:
    pc.create_index(
        name=INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

# Load Pinecone index
index = pc.Index(INDEX_NAME)

# Sample text
raw_text = "LangChain enables retrieval-augmented generation (RAG) with Pinecone. It's useful for LLM-powered apps."
splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
texts = splitter.split_text(raw_text)
docs = [Document(page_content=t) for t in texts]

# Embeddings
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Vector store
vectorstore = PineconeVectorStore(
    index=index,
    embedding=embedding,
    text_key="text",
    namespace=NAMESPACE
)

# Add documents
vectorstore.add_documents(docs)
print("✅ Successfully added documents to Pinecone using new API.")

# Build LLM + QA chain
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

# Run sample query
query = "What is the sample text about?"
result = qa_chain.invoke({"query": query})
print("\n📄 Query Result:\n", result['result'])