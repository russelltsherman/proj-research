from llm.agents import BaseAgent
from llm.models import OllamaChat
from langchain.prompts.chat import ChatPromptTemplate
import datetime as dt

class ADRWriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(model=OllamaChat())

    def system_prompt(self):

        with open("llm/prompts/adr-writer.txt", "r") as file:
            content = file.read()

        template = ChatPromptTemplate([
            ("system", content),
        ])

        return template.invoke({"date": dt.date.today()}).messages[0].content

