import psycopg2

DATABASE_URL = "postgresql://test:test@db:5432/test"

def get_connection():
    return psycopg2.connect(DATABASE_URL)
