# import re
# import numpy as np
# from pydub import AudioSegment
# from flask import Flask, request, jsonify, send_file
# import json

# app = Flask(__name__)


# @app.route('/image_endpoint', methods=['POST'])
# def visualize_paragraph():
#     paragraph_text = request.form['paragraph']
#     title = request.form['title']
#     image_context = generate_SummarizedPrompt_image(paragraph_text, title)
#     print(image_context)

#     image_data = imggen(image_context)

#     return jsonify({'image': image_data})


# # generate_SummarizedPrompt_image(
# #     paragraph_text, title)
# generate_SummarizedPrompt_audio(paragraph_text)

# if __name__ == '__main__':
#     app.run()

from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from answer_gen import query_llm
from fastapi import FastAPI, Form, HTTPException
app = FastAPI()


@app.post('/ask_doubt')
async def query_RAGLLM(courseID: str = Form(...), question: str = Form(...)):
    # print(type(courseID),type(question))
    response = query_llm(courseID, question)
    return {'response': response}