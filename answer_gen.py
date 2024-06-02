from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def query_llm(cid,quest):
    API_KEY= ''
    embed1 = OpenAIEmbeddings(openai_api_key=API_KEY)
    vs = FAISS.load_local(str(cid),embeddings=embed1,allow_dangerous_deserialization=True)
    llm = ChatOpenAI(openai_api_key=API_KEY)
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vs.as_retriever(),
        memory=memory
    )
    result = conversation_chain({"question":str(quest)})['answer']
    # print(result)
    return result