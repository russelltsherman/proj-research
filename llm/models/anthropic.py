from langchain_anthropic import ChatAnthropic
import os

class Anthropic(ChatAnthropic):
    def __init__(self, **kwargs):
        super().__init__(
            api_key = os.getenv('ANTHROPIC_API_KEY', kwargs.get('api_key', None)) ,
            model = kwargs.get('model', 'claude-3-5-sonnet-latest'), 
            temperature=kwargs.get('temperature', 0)
            # max_retries=2,
            # max_tokens=None,
            # timeout=None,
            # # base_url="...",
            # # other params...
            )

