PROMPT_VERSION = "V1.0.0"



def build_prompt(resume_text: str)->str:
    return f"""
You are an expert technical recruiter.

Analyze the resume below and extract:

- Candidate name
- Top skills
- Years of experience
- Seniority level (junior, mid, senior)
- Strengths
- Skill gaps
- Overall score (0-10)

Resume:
{resume_text}
"""