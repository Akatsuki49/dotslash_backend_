from langchain_community.document_loaders import PDFMinerLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings,HuggingFaceInstructEmbeddings
# import torch
# from langchain_community.document_loaders import PDFMinerLoader
from langchain.vectorstores import Chroma,FAISS
from langchain.chat_models import ChatOpenAI
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv
from transcriber import transcribe
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
API_KEY = ""
text=""
text2 = transcribe("./UE21CS351B.mp3")
list1=[]
text1 = "The Speaker says everything which follows:"+text2
pdf_reader=PdfReader("./UE21CS351B.pdf")
for page in pdf_reader.pages:
    text+=page.extract_text()
# x1 = data[0].page_content
cleaned_content = text.replace('\n\n\x0c', '\n\n\n').replace('\n\n', '\n')
text_splitter = CharacterTextSplitter(
    chunk_size = 512,
    chunk_overlap  = 24,
    length_function = len,
    separator="\n"
)
text_splitter1 = CharacterTextSplitter(
    chunk_size = 512,
    chunk_overlap  = 24,
    length_function = len,
    separator="\n"
)

chunks = text_splitter.split_text(cleaned_content)
chunks1 = text_splitter.split_text(text1)
embeddi = OpenAIEmbeddings(openai_api_key=API_KEY)
vectorst = FAISS.from_texts(texts=chunks,embedding=embeddi)
vectorst.add_texts(texts=chunks1)
vectorst.save_local("UE21CS351B")
# print(type(vectorst))
# print(result['answer'])