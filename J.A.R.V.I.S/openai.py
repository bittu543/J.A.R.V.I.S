import os
import openai
from openai import openai

openai.api_key = os.getenv("open ai api key")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="",
  temperature=0.7,
  max_tokens=256,
)
