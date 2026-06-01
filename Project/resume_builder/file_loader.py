from pathlib import Path


def load_resumes():

    resume_dir = Path(__file__).parent / "resumes"

    resumes = []

    for file in resume_dir.glob("*.txt"):

        content = file.read_text(
            encoding="utf-8"
        )

        resumes.append(
            {
                "filename": file.name,
                "content": content
            }
        )

    return resumes