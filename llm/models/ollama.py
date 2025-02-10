from langchain_community.chat_models import ChatOllama


class OllamaChat(ChatOllama):
    def __init__(self):
        super().__init__( 
            api_key='unnecessary',
            base_url='http://localhost:11434',
            model='llama3.2', 
            temperature='0'
        )
