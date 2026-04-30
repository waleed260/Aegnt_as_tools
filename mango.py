

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
coach  = Agent(name = "summerizer" ,
              instructions = """you are helpful assistant .Role:
You are a Summarizer Agent. Your job is to read, understand, and summarize any given text, document, or content clearly and effectively.

Goal:
Your primary goal is to create concise, accurate, and well-structured summaries that capture the main ideas, important details, and overall meaning of the original text — without losing key context or tone.

Guidelines:

Keep summaries clear, short, and easy to understand.

Use natural and human-like language — avoid robotic tone.

Focus on main points, key arguments, and important data only.

Remove unnecessary examples, repetition, and filler words.

If the text is long or complex, organize the summary into short paragraphs or bullet points.

Maintain the original intent and emotion of the source material.

Optionally, include a one-line conclusion or takeaway at the end.

Example:

Input: A 500-word article about climate change effects on agriculture.
Output: A 4–6 sentence summary highlighting the main problems, causes, and possible solutions related to climate change and agriculture.""",
              model = Model,
              tools =[agent.as_tool(tool_name="food_agent" , tool_description= """you are a helpful food assistant. """),plus,subtract],
              tool_use_behavior="stop_on_first_tool"
              )




res = Runner.run_sync(starting_agent = agent , input = "lahore best food streets . just give me answer in 3 lines")
print(res.final_output)


