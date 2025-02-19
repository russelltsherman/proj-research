from langchain_openai import ChatOpenAI
import os


class Gemini(ChatOpenAI):
    def __init__(self, **kwargs):
        super().__init__( 
            api_key = os.getenv('GEMINI_API_KEY', kwargs.get('api_key', None)) ,
            base_url = 'https://generativelanguage.googleapis.com/v1beta/openai/',
            model = kwargs.get('model', 'gemini-2.0-flash-exp'),
            temperature=kwargs.get('temperature', 0)
            # max_retries=2,
            # max_tokens=None,
            # timeout=None,
        )
