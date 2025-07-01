
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


def get_qa_chain(session_id: str):
    vectordb = Chroma(persist_directory=f"vector_store/{session_id}", embedding_function=OpenAIEmbeddings())
    retriever = vectordb.as_retriever()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return ConversationalRetrievalChain.from_llm(ChatOpenAI(temperature=0), retriever=retriever, memory=memory)
 