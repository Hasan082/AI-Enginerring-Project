from resume_analyser import analyze_resume
from prompts import build_prompt


resumes = [
    """
    John Smith

    Senior Software Engineer

    Skills:
    Python, Django, AWS

    Experience:
    7 years
    """,

    """
    Sarah Ahmed

    Data Analyst

    Skills:
    SQL, Power BI, Excel

    Experience:
    3 years
    """,

    """
    David Lee

    Junior Developer

    Skills:
    HTML, CSS, JavaScript

    Experience:
    1 year
    """
]


results = []
for resume in resumes:
    prompt = build_prompt(resume)
    result = analyze_resume(prompt)
    results.append(result)




print(results)