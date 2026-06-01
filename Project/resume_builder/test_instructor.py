from pydantic import BaseModel
from llm import client
import os
from dotenv import load_dotenv

load_dotenv()

class Person(BaseModel):
    name: str
    profession: str


result = client.chat.completions.create(
    model=os.getenv("GROQ_MODEL"),
    response_model=Person,
    messages=[
        {
            "role": "user",
            "content": "John is software engineer"
        }
    ]
)

print(result)
print(type(result))