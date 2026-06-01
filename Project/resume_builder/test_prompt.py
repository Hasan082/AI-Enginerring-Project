from prompts import build_prompt


resume_text = """
John Smith

Senior Software Engineer

Skills:
Python
Django
AWS
PostgreSQL

Experience:
7 years
"""

prompt = build_prompt(resume_text)
print(prompt)