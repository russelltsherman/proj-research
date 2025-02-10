from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI


class OllamaChat(ChatOpenAI):
    def __init__(self):
        super().__init__( 
            api_key='unnecessary',
            base_url='http://localhost:11434/v1',
            model='llama3.2', 
            temperature='0'
        )
