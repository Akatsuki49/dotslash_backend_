from langchain.chat_models import ChatOpenAI
import faiss
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import os
from langchain.embeddings import OpenAIEmbeddings
import numpy as np
from langchain.vectorstores import FAISS

API_KEY=os.getenv("OPENAI_API_KEY")
embed1 = OpenAIEmbeddings(openai_api_key=API_KEY)
vs = FAISS.load_local('db1',embeddings=embed1)
# ind = faiss.read_index("./db1/index.faiss")
# vs = FaissVectorStore(ind)
llm = ChatOpenAI(openai_api_key=API_KEY)
memory = ConversationBufferMemory(
    memory_key='chat_history', return_messages=True)
conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vs.as_retriever(),
    memory=memory
)
result = conversation_chain({"question":"What is REST?"})['answer']