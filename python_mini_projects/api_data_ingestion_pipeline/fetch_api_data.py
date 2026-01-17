import requests
import json
import logging
from datetime import datetime
from pathlib import Path

# ---------------- LOGGING ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

API_URL = "https://fakestoreapi.com/users"

# ---------------- PROJECT ROOT ----------------
BASE_DIR = Path(__file__).resolve().parent

RAW_BASE_PATH = BASE_DIR / "raw" / "users"

def fetch_users():
    logging.info("Calling users API")
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()

def write_raw(users):
    ingestion_date = datetime.utcnow().date().isoformat()

    raw_path = RAW_BASE_PATH / f"ingestion_date={ingestion_date}"
    raw_path.mkdir(parents=True, exist_ok=True)

    file_path = raw_path / "users_raw.json"

    with open(file_path, "w") as f:
        json.dump(users, f, indent=2)

    logging.info(f"Raw data written to {file_path}")

if __name__ == "__main__":
    logging.info("RAW ingestion started")
    users = fetch_users()
    write_raw(users)
    logging.info("RAW ingestion completed")
