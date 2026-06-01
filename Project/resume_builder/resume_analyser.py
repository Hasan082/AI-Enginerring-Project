from tenacity import retry, stop_after_attempt, wait_exponential
from llm import client
from scemas import CandidateProfile
import os
from dotenv import load_dotenv

load_dotenv()


@retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(
            multiplier=1,
            min=2,
            max=10
        )
)
def analyze_resume(prompt):
    result = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL"),
        response_model=CandidateProfile,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return result

