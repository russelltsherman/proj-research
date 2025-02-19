from langchain_groq import ChatGroq
import os


class Groq(ChatGroq):
    def __init__(self, **kwargs):
        super().__init__(
            api_key = os.getenv('GROQ_API_KEY', kwargs.get('api_key', None)) ,
            model = kwargs.get('model', 'llama3-70b-8192'), 
            temperature=kwargs.get('temperature', 0)
            # max_retries=2,
            # max_tokens=None,
            # timeout=None,
            # # base_url="...",
            # # other params...
            )

# Key init args — completion params:
# model: str
# Name of Groq model to use. E.g. “mixtral-8x7b-32768”.

# temperature: float
# Sampling temperature. Ranges from 0.0 to 1.0.

# max_tokens: Optional[int]
# Max number of tokens to generate.

# model_kwargs: Dict[str, Any]
# Holds any model parameters valid for create call not explicitly specified.

# Key init args — client params:
# timeout: Union[float, Tuple[float, float], Any, None]
# Timeout for requests.

# max_retries: int
# Max number of retries.

# api_key: Optional[str]
# Groq API key. If not passed in will be read from env var GROQ_API_KEY.

# base_url: Optional[str]
# Base URL path for API requests, leave blank if not using a proxy or service emulator.

# custom_get_token_ids: Optional[Callable[[str], List[int]]]
# Optional encoder to use for counting tokens.
