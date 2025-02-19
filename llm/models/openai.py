from langchain_openai import ChatOpenAI
import os


class OpenAI(ChatOpenAI):
    def __init__(self, **kwargs):
        super().__init__( 
            api_key = os.getenv('OPENAI_API_KEY', kwargs.get('api_key', None)),
            model = kwargs.get('model', 'gpt-4o-mini'),
            temperature=kwargs.get('temperature', 0)
            # max_retries=2,
            # max_tokens=None,
            # timeout=None,
        )
      