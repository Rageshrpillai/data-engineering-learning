# API to PostgreSQL Ingestion Pipeline

## Overview

This project implements a **production-style ingestion pipeline** that synchronizes user data from an external REST API into PostgreSQL.

The pipeline treats the database as a **system of record** and ensures:

- strict validation before load
- idempotent writes using UPSERT
- transactional safety (commit / rollback)
- fail-fast behavior on errors

This is an **operational ingestion pipeline**, not an analytical ETL job.

---

## Architecture

API → Validation → PostgreSQL (UPSERT)

### Responsibilities

- **API Client**: Fetches data from external API
- **Validation Layer**: Enforces required fields and blocks bad data
- **Loader**: Writes data using idempotent UPSERT logic
- **Database**: Enforces primary key and long-term consistency
- **Main**: Orchestrates the pipeline and configures logging

---

## Database Schema

The required table must be created **once** before running the pipeline.

```sql
CREATE TABLE IF NOT EXISTS users (
    id          INTEGER PRIMARY KEY,
    name        TEXT,
    email       TEXT NOT NULL,
    updated_at  TIMESTAMP NOT NULL
);
```
