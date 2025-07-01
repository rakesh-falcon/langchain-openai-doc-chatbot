import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
 
VECTOR_DIR = "vector_store"
 
def store_pdf_in_chroma(session_id: str, texts: list[str]):
    os.makedirs(VECTOR_DIR, exist_ok=True)
 
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = [Document(page_content=t) for text in texts for t in splitter.split_text(text)]
 
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(docs, embeddings, persist_directory=f"{VECTOR_DIR}/{session_id}")
    vectordb.persist()
    vectordb = None  # Clear memory