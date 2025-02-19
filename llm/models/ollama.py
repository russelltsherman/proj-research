from langchain_openai import ChatOpenAI
import os

class Ollama(ChatOpenAI):
    def __init__(self, **kwargs):
        super().__init__( 
            api_key = 'unnecessary',
            base_url = os.getenv('OLLAMA_BASE_URL', kwargs.get('base_url', 'http://localhost:11434/v1')),
            model = kwargs.get('model', 'llama3.2'), 
            temperature = kwargs.get('temperature', 0)
            # max_retries=2,
            # max_tokens=None,
            # timeout=None,
        )
