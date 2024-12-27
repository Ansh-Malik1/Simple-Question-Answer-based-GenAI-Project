import os
from dotenv import load_env
from langchain_community.llms import Ollama
import streamlit as stl
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_env()



os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRAICING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Hey you are a helpful assistant. Please respond to the question asked."),
        ("user","Question:{question}")
    ]
)

stl.title("Langchain Demo with Gemma:2b")
input_text = stl.text_input("What question do you have?")


llm = Ollama(model = "gemma:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    stl.write(chain.invoke({"question":input_text}))
    
    
