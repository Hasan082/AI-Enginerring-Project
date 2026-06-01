# AI Resume Analyzer

A production-oriented AI Resume/CV Analyzer that extracts structured candidate insights from PDF or plain-text resumes using LLMs, Pydantic, Instructor, and OpenAI/Anthropic APIs.

---

## Project Objective

Build an AI-powered resume analysis system capable of:

* Accepting PDF or text resumes as input
* Extracting structured candidate information
* Returning strongly typed outputs using Pydantic
* Providing reliability through retries and validation
* Logging usage metrics for observability
* Supporting intelligent model routing for cost optimization

This project simulates a real-world HR Tech freelance deliverable commonly used for candidate screening and recruitment workflows.

---

## Architecture

```text
Resume PDF/TXT
      ↓
Text Extraction
      ↓
Prompt Builder
      ↓
Model Router
      ↓
GPT-3.5 / GPT-4o
      ↓
Instructor + Pydantic
      ↓
CandidateProfile
      ↓
JSON Logs
      ↓
Database/API/UI
```

---

## Features

### 1. Resume Input

Support:

* PDF resumes
* Plain text resumes

Example:

```text
John Smith
Senior Software Engineer

Skills:
Python, Django, AWS, PostgreSQL

Experience:
7 years
```

---

### 2. Structured Output with Pydantic

Define a typed schema:

```python
class CandidateProfile(BaseModel):
    name: str
    top_skills: list[str]
    years_experience: int
    seniority_level: Literal[
        "junior",
        "mid",
        "senior"
    ]
    strengths: list[str]
    gaps: list[str]
    overall_score: float
```

Expected output:

```json
{
  "name": "John Smith",
  "top_skills": [
    "Python",
    "Django",
    "AWS"
  ],
  "years_experience": 7,
  "seniority_level": "senior",
  "strengths": [
    "Backend Development",
    "Cloud Architecture"
  ],
  "gaps": [
    "Kubernetes"
  ],
  "overall_score": 8.7
}
```

---

### 3. Prompt Builder

Create reusable and versioned prompts.

Responsibilities:

* Inject resume text
* Define extraction requirements
* Control output format
* Enable prompt versioning

Example:

```python
PROMPT_VERSION = "v1.0"
```

---

### 4. Instructor + OpenAI / Anthropic

Use Instructor to enforce structured outputs.

Benefits:

* Automatic schema validation
* Strongly typed responses
* Reduced parsing complexity
* Production reliability

Output should return:

```python
CandidateProfile(...)
```

instead of raw text.

---

### 5. Retry and Resilience

Use Tenacity for retry handling.

Requirements:

* Exponential backoff
* Automatic retry on:

  * Rate limits
  * API timeouts
  * Temporary provider failures

Example:

```python
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(
        multiplier=1,
        min=2,
        max=10
    )
)
```

---

### 6. Observability and Logging

Every LLM call must be logged as structured JSON.

Required log format:

```json
{
  "timestamp": "2026-06-01T12:00:00Z",
  "model": "gpt-4o",
  "latency_ms": 1240,
  "tokens_used": 950,
  "seniority_level": "senior"
}
```

Store logs locally:

```text
logs/resume_analysis.jsonl
```

---

### 7. Resume Comparison

Process at least three resumes.

Generate a comparison table:

| Candidate   | Experience | Seniority | Score |
| ----------- | ---------- | --------- | ----- |
| John Smith  | 7 Years    | Senior    | 8.7   |
| Sarah Ahmed | 4 Years    | Mid       | 7.4   |
| David Lee   | 1 Year     | Junior    | 5.8   |

---

## Stretch Goal: Model Router

Implement dynamic model selection.

### Routing Rules

```text
Resume < 500 words
→ GPT-3.5 Turbo

Resume >= 500 words
→ GPT-4o
```

Benefits:

* Reduced cost
* Faster processing
* Better scalability

---

## Tech Stack

### Core

* Python 3.12+
* Pydantic v2
* Instructor
* OpenAI API
* Anthropic API
* Tenacity

### Optional

* LiteLLM
* Langfuse
* LangSmith
* PostgreSQL
* FastAPI
* Celery
* Redis

---

## Learning Outcomes

By completing this project you will learn:

* Pydantic schema design
* Structured LLM outputs
* Prompt engineering
* Retry strategies
* Observability and logging
* Cost-aware model routing
* Production AI architecture

---

## Deliverables

* Resume ingestion pipeline
* CandidateProfile schema
* Prompt builder module
* Model router
* Instructor integration
* Retry handling with Tenacity
* Structured JSON logging
* Resume comparison report
* Documentation and README

---

## Future Enhancements

* Job description matching
* ATS compatibility scoring
* Candidate ranking
* Resume embedding search
* RAG-based recruitment assistant
* FastAPI backend
* React dashboard
* Multi-provider fallback (OpenAI → Anthropic → Gemini)

```
```
