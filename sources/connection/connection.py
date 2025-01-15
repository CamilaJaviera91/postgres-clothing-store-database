import psycopg2
from psycopg2 import OperationalError

def connection():
    try:
        conn = psycopg2.connect(
            host="localhost",           # Address of the PostgreSQL server (localhost for local machine)
            database="postgres",        # Name of the database to connect to
            user="admin",            # Database username
            password="admin123",            # Password for the user
            port="5432"                 # Port PostgreSQL is listening on (default is 5432)
        )
        print("Connection Successful")
        return conn
    
    except OperationalError as e:
        print(f"Database connection failed {e}")
        return None