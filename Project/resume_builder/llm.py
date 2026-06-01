from groq import Groq
import instructor
import os
from dotenv import load_dotenv
load_dotenv()


client = instructor.from_groq(
    Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )
)