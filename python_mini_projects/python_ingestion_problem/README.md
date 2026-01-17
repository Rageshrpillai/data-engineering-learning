# Python to PostgreSQL Ingestion Pipeline (Idempotent UPSERT)

This mini project demonstrates how to ingest structured data into PostgreSQL using Python,
while ensuring idempotency, duplicate prevention, and production-style logging.

## Project Overview

The goal of this project is to understand how Python interacts with a relational database
and how databases should own data correctness rules such as uniqueness and updates.

The pipeline reads source data, connects to PostgreSQL, and performs an UPSERT operation
to safely handle inserts and updates without creating duplicates.

## Key Concepts Covered

- Python database connectivity using psycopg2
- Idempotent pipeline design
- Duplicate prevention using primary keys
- PostgreSQL `ON CONFLICT` UPSERT
- Proper ownership of logic (DB vs Python)
- Production-style logging and error handling

## Project Flow

Source Data
↓
Python (read + prepare)
↓
PostgreSQL (UPSERT + constraints)

## Idempotency

The pipeline is idempotent, meaning:

- Running it multiple times produces the same final database state
- Duplicate records are prevented using a primary key
- Updates are handled safely using database-level conflict resolution

## Why UPSERT is Handled by PostgreSQL

Instead of Python checking whether a record exists, PostgreSQL enforces uniqueness
and decides whether to insert or update data. This approach is:

- Faster
- Atomic
- Safe under concurrent executions

## Logging and Observability

The pipeline uses structured logging to record:

- Pipeline start and completion
- Database connection status
- Number of records processed
- Insert and update outcomes

This makes the pipeline suitable for production monitoring and debugging.

## How to Run

1. Ensure PostgreSQL is running
2. Update database connection details in the script
3. Run the pipeline:

```bash
python load_customer.py
```
