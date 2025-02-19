from langchain_openai import ChatOpenAI
import os


class Deepseek(ChatOpenAI):
    def __init__(self, **kwargs):
        super().__init__( 
            api_key = os.getenv('DEEPSEEK_API_KEY', kwargs.get('api_key', None)) ,
            base_url = 'https://api.deepseek.com',
            model = kwargs.get('model', 'deepseek-chat'), 
            temperature=kwargs.get('temperature', 0)
            # max_retries=2,
            # max_tokens=None,
            # timeout=None,
            )
