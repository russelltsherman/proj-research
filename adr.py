from colorama import Fore
import datetime as dt
from devtools import debug
from llm.agents.adr import ADRWriterAgent


agent = ADRWriterAgent()

def stream_response(prompt):
    print(Fore.LIGHTGREEN_EX + '\nASSISTANT: \n')
    agent.stream(prompt)


def main():
    while True:
        prompt = input(Fore.WHITE + '\nUSER: \n')

        terms = ['exit', 'bye', 'quit']
        if prompt.lower() in terms:
            print("Goodbye!")
            break

        stream_response(prompt)


if __name__ == "__main__":
    main()
