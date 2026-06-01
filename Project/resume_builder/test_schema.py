from scemas import CandidateProfile

candidate = CandidateProfile(
    name="Md Hasan",
    top_skill=["python", "django", "aws"],
    experience=7,
    seniority_level="senior",
    strengths=["Backend", "System design"],
    gaps=[
        "kuburnets"
    ],
    overall_score=8.7
)
print(candidate)

candidate2 = CandidateProfile(
    name="John Smith",
    top_skills=["Python"],
    years_experience=-5,
    seniority_level="expert",
    strengths=[],
    gaps=[],
    overall_score=15
)


print(candidate2)