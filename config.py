from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
from tools import tools

load_dotenv()


BASE_URL = os.getenv("BASE_URL")
MODEL = os.getenv("MODEL")
API_KEY = os.getenv("API_KEY")

def get_llm():
    llm = ChatOpenAI(
        base_url=BASE_URL,  
        model=MODEL,
        api_key=API_KEY,
        temperature=0
        ).bind_tools(tools)
    
    return llm

