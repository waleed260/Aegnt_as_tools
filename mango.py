

from agents import AsyncOpenAI , OpenAIChatCompletionsModel,  Runner, Agent ,set_tracing_disabled  
from tools import plus , subtract
from rich import print
from dotenv import load_dotenv
import os
from dataclasses import dataclass
from pydantic import BaseModel
set_tracing_disabled(True)
load_dotenv()






key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")


Gemini_client = AsyncOpenAI(api_key = key ,base_url= base_url)
Model = OpenAIChatCompletionsModel(model = "gemini-2.5-flash", openai_client = Gemini_client)
agent = Agent(name = """food agent ,and tasty recipes for any type of food. 
              Each recipe should start with a short introduction about the dish, then list all the ingredients with proper measurements, and give step-by-step cooking instructions.
              You should also share helpful cooking tips, healthy alternatives, and serving ideas.
              Your tone should be friendly and professional, making it easy for beginners and home cooks to understand and enjoy cooking
              instructions = you are helpful assistant .
              You are a Food Recipe Agent.Your job is to create clear, easy-to-follow . """,
              model = Model,
            
              )
