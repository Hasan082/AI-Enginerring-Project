import time
import os
from tenacity import retry, stop_after_attempt, wait_exponential
from llm import client
from scemas import CandidateProfile
from logger import log_resume_analyser
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
def analyze_resume(prompt) -> CandidateProfile:

    start = time.time()

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
    latency_ms = round(
        (time.time() - start) * 1000
    )

    log_resume_analyser(
         model=os.getenv("GROQ_MODEL"),
         latency_ms=latency_ms,
         seniority_level=result.seniority_level
    )

    return result

