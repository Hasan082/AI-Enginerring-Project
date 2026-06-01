from llm import client
from scemas import CandidateProfile
from prompts import build_prompt, PROMPT_VERSION
from resume_analyser import analyze_resume



resume = """
John Smith

Senior Software Engineer

Skills:
Python
Django
AWS
PostgreSQL

Experience:
7 years

Built scalable backend systems.
Led engineering teams.
"""

prompt = build_prompt(resume)


print(f"Using Prompt Version: {PROMPT_VERSION}")


result = analyze_resume(prompt)

print(result)