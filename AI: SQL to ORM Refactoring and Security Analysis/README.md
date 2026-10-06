# AI: SQL to ORM Refactoring and Security Analysis

## Objective
Use an AI assistant to refactor a procedural MySQL script (raw SQL via
mysql.connector) into an object-oriented SQLAlchemy ORM version, and
analyse the security and professional benefits.

## Files
- `initial_sql.py`: original procedural script using raw SQL
- `refactored_orm.py`: AI-assisted SQLAlchemy 2.x ORM refactor

## What changed
- SQL strings replaced by a declarative `User` model
- Table created with `Base.metadata.create_all()`
- All CRUD functions use an ORM `Session`, with `s.begin()` for automatic
  commit/rollback
- Credentials read from environment variables instead of hard-coded

## Key takeaways
- The ORM always sends values as bound parameters, so safe queries are
  the default, not something each developer must remember
- The schema is defined once in the `User` class, so changes happen in
  one place
- Swapping the database URL makes the code portable and easy to test
  with in-memory SQLite

## How to run
    pip install sqlalchemy mysql-connector-python
    export DB_USER=... DB_PASSWORD=... DB_NAME=...
    python3 refactored_orm.py
