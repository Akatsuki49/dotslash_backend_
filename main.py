
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from answer_gen import query_llm
from fastapi import FastAPI, Form, HTTPException, Response
from tts import tts1
app = FastAPI()


@app.post('/ask_doubt')
async def query_RAGLLM(courseID: str = Form(...), question: str = Form(...)):
    # print(type(courseID),type(question))
    response = query_llm(courseID, question)
    # tts1(response)
    # with open("output.wav", "rb") as wav_file:
    #     wav_data = wav_file.read()
    # headers = {
    # "Content-Disposition": "attachment; filename=output.wav",
    # "Content-Type": "audio/wav",
    # }
    # return {"o1":Response(content=wav_data,headers=headers),"o2":response}
    return response