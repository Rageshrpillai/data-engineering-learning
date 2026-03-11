import json
import pandas as pd
import logging
from pathlib import Path

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ---------------- BASE PATHS (PRODUCTION SAFE) ----------------
BASE_DIR = Path(__file__).resolve().parent
RAW_BASE_PATH = BASE_DIR / "raw" / "users"
CURATED_BASE_PATH = BASE_DIR / "curated"


# ---------------- READ LATEST RAW DATA ----------------
def read_latest_raw():
    ingestion_folders = sorted(RAW_BASE_PATH.glob("ingestion_date=*"))

    if not ingestion_folders:
        raise FileNotFoundError("No raw ingestion folders found")

    latest_folder = ingestion_folders[-1]
    raw_file = latest_folder / "users_raw.json"

    logging.info(f"Reading raw file: {raw_file}")

    with open(raw_file, "r") as f:
        return json.load(f)


# ---------------- FLATTEN USERS (STRICT SCHEMA) ----------------
def flatten_users(users):
    """
    Strict flattening:
    - No guessing
    - No fixing
    - Missing fields become None
    """

    flattened = []

    for user in users:
        record = {
            "user_id": user.get("id"),
            "email": user.get("email"),
            "username": user.get("username"),
            "phone": user.get("phone"),
            "first_name": user.get("name", {}).get("firstname"),
            "last_name": user.get("name", {}).get("lastname"),
            "city": user.get("address", {}).get("city"),
            "zipcode": user.get("address", {}).get("zipcode"),
        }
        flattened.append(record)

    return flattened


# ---------------- MAIN CURATED PIPELINE ----------------
if __name__ == "__main__":
    logging.info("CURATED ingestion started")

    # Step 1: Read raw data
    raw_users = read_latest_raw()

    # Step 2: Flatten raw records
    flattened_users = flatten_users(raw_users)
    logging.info(f"Flattened records count: {len(flattened_users)}")

    # Step 3: Convert to DataFrame
    df = pd.DataFrame(flattened_users)

    logging.info("Converted flattened records to Pandas DataFrame")
    logging.info(f"DataFrame shape: {df.shape}")
    logging.info(f"Columns: {list(df.columns)}")

    logging.info("DataFrame dtypes:")
    logging.info(df.dtypes)

    # ---------------- SCHEMA EXPECTATIONS ----------------
    MANDATORY_COLUMNS = ["user_id", "email"]
    OPTIONAL_COLUMNS = [
        "username",
        "phone",
        "first_name",
        "last_name",
        "city",
        "zipcode"
    ]

    # ---------------- VALIDATION (OBSERVABILITY ONLY) ----------------
    missing_user_id = df["user_id"].isna().sum()
    missing_email = df["email"].isna().sum()

    logging.info(f"Missing user_id count: {missing_user_id}")
    logging.info(f"Missing email count: {missing_email}")

    if missing_user_id > 0:
        logging.warning("Some records are missing user_id (critical field)")

    if missing_email > 0:
        logging.warning("Some records are missing email (critical field)")

    # ---------------- WRITE CURATED OUTPUT ----------------
    CURATED_BASE_PATH.mkdir(exist_ok=True)

    output_file = CURATED_BASE_PATH / "users_curated.csv"
    df.to_csv(output_file, index=False)

    logging.info(f"Curated data written to {output_file}")
    logging.info("CURATED ingestion completed")
