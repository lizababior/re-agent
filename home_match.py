#A starter file for the HomeMatch application if you want to build your solution in a Python program instead of a notebook. 

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model_name = "gpt-3.5-turbo"
temperature = 0.0
llm = ChatOpenAI(model_name=model_name, temperature=temperature, max_tokens = 500)