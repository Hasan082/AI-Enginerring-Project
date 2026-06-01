from pydantic import BaseModel, Field
from typing import Literal


class CandidateProfile(BaseModel):
    name: str
    top_skill: list[str]
    experience: int = Field(
        ge=0,
        le=50
    )
    seniority_level: Literal["entry", "mid", "senior"]
    strengths: list[str]
    gaps: list[str]
    overall_score: float = Field(
        ge=0,
        le=10
    )
