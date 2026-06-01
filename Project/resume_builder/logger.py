import json
from datetime import datetime, timezone
from pathlib import Path

LOG_FILE = Path(__file__).parent / "resume_logs.jsonl"

def log_resume_analyser(model: str, latency_ms: int, seniority_level: str):
    log_record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "latency_ms": latency_ms,
        "seniority_level": seniority_level
    }
    print("Logging...")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_record)+ "\n") 

