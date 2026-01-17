# API Raw to Curated Ingestion Pipeline

This mini project demonstrates a production-style data ingestion pipeline that separates
raw data ingestion from curated data processing.

## Project Overview

The pipeline follows a layered architecture:

API → Raw (immutable JSON) → Curated (validated tabular data)

This design ensures:

- Raw source data is preserved
- Curated data can be reprocessed safely
- Schema changes do not require re-fetching data

## Project Structure

```

api_data_ingestion_pipeline/
│
├── fetch_raw_users.py        # Fetches API data and stores raw JSON
├── curate_users.py           # Builds curated dataset from raw data
│
├── raw/
│   └── users/
│       └── ingestion_date=YYYY-MM-DD/
│           └── users_raw.json
│
├── curated/
│   └── users_curated.csv

```

## Pipeline Steps

### 1. Raw Ingestion

- Fetches data from an external API
- Stores the response exactly as received
- Data is partitioned by ingestion date
- Raw data is immutable

### 2. Curated Ingestion

- Reads the latest raw data
- Flattens nested JSON fields
- Applies a strict schema
- Uses Pandas for data inspection and validation
- Writes a curated CSV output

## Data Validation

Mandatory fields:

- `user_id`
- `email`

Validation is observational only:

- Missing values are logged
- Data is not altered or guessed

## How to Run

```bash
python fetch_raw_users.py
python curate_users.py
```

The curated pipeline can be re-run any time without re-calling the API.

## Key Concepts Demonstrated

- Separation of concerns
- Raw vs curated data layers
- Idempotent reprocessing
- Schema enforcement using Pandas
- Production-safe file path handling
