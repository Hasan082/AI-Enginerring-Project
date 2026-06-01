# Build a CV/Resume Analyzer with structured output and observability.

# Take any PDF or plain-text resume as input.
# Define a Pydantic model: CandidateProfile with fields like name, top_skills: list[str], years_experience: int, seniority_level: Literal["junior","mid","senior"], strengths: list[str], gaps: list[str], overall_score: float.
# Write a prompt builder that injects the resume text.
# Use instructor + OpenAI or Anthropic to return a typed CandidateProfile.
# Add tenacity retry with exponential backoff.
# Log every call as structured JSON to a local file: {timestamp, model, latency_ms, tokens_used, seniority_level}.
# Run it on 3 different resumes and compare outputs.

# Stretch goal: Add a model router that uses gpt-3.5-turbo for resumes under 500 words and gpt-4o for longer ones.
# This is a real freelance deliverable. HR tech clients pay well for exactly this.

# Resume PDF/TXT
#       ↓
# Text Extraction
#       ↓
# Prompt Builder
#       ↓
# Model Router
#       ↓
# GPT-3.5 / GPT-4o
#       ↓
# Instructor + Pydantic
#       ↓
# CandidateProfile
#       ↓
# JSON Logs
#       ↓
# Database/API/UI