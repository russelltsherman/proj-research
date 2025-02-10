from colorama import Fore
import datetime as dt
from devtools import debug
from langchain_core.prompts import ChatPromptTemplate
from llm.models import OllamaChat

system_prompt = (
    'You are an expert software architect specializing in Python-based systems. '
    'Your task is to write clear, structured, and concise Architectural Decision Records (ADRs) '
    'that document key architectural choices for Python applications. '
    'Guidelines: '
    f"Todays date is {dt.datetime.today().strftime('%Y-%m-%d')} "
    'Focus on Python-specific architectural concerns, such as framework selection (Django, FastAPI, Flask), '
    'dependency management, performance, security, scalability, and deployment strategies. '
    'Justify decisions with technical reasoning and trade-offs while maintaining clarity and brevity. '
    'Ensure ADRs remain useful for future teams by providing sufficient but concise context and rationale. '
    'Use precise language, avoiding unnecessary jargon. ' 
    'Each ADR must follow this format: '
    '\n# [Title] '
    '\n\nDate: [Todays Date]'
    '\n\n## Status\n\nAccepted'
    '\n\n## Context\n\n[Summarize the problem and relevant considerations (maximum four sentences).]'
    '\n\n## Decision\n\n[Summary of the chosen solution or approach (maximum four sentences)]'
    '\n\n## Consequences\n\n[Summary of the trade-offs and impact of this decision (maximum four sentences).]'
    ''
    'always adhere to the defined format. '
    'do not deviate from the defined format. '
)

prompt = ChatPromptTemplate([
    ("system", system_prompt),
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
    
