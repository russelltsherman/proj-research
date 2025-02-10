from colorama import Fore
from devtools import debug
from langchain_core.prompts import ChatPromptTemplate
from llm.models import OllamaChat


prompt = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    ("user", "{prompt}")
])
model = OllamaChat()
chain = prompt | model


"""
handle streaming responses
"""
def stream_response(prompt):
    print(Fore.LIGHTGREEN_EX + '\nASSISTANT: \n')
    response = []

    for chunk in chain.stream(prompt):
        response.append(chunk.content)
        print(chunk.content, end="", flush=True)

    print('\n')


"""
application entrypoint
"""
def chat():
    while True:
        prompt = input(Fore.WHITE + '\nUSER: \n')

        terms = ['exit', 'bye', 'quit']
        if prompt.lower() in terms:
            print("Goodbye!")
            break

        stream_response(prompt)


if __name__ == "__main__":
    chat()
    
