CREATE TABLE IF NOT EXISTS users (
    id          INTEGER PRIMARY KEY,
    name        TEXT,
    email       TEXT NOT NULL,
    updated_at  TIMESTAMP NOT NULL
);