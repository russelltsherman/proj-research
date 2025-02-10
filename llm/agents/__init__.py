from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from typing import List
from devtools import debug


class BaseAgent():
    def __init__(self, model):
        self.model = model

    def format_user_message(self, message):
        output = ""
        if type(message)==str:
            output = [
                SystemMessage(content=self.system_prompt()),
                HumanMessage(content=message)
            ]
        elif type(message)==List:
            pass
        return(output)
        
    def system_prompt(self):    
        return (
            'You are an helpful assistant'
        )
    
    def invoke(self, message):
        return self.model.invoke(input=self.format_user_message(message))

    def stream(self, message):
        response=[]
        for chunk in self.model.stream(self.format_user_message(message)):
            response.append(chunk.content)
            print(chunk.content, end="", flush=True)
        print('\n')

