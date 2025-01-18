# Import the connection function from the 'connection' file
import sys
sys.path.append('./sources/connection/')

from connection import connection

# Import necessary libraries
import psycopg2
import locale
import pandas as pd

def query_suppliers_q():
    # Set the locale to Spanish (Spain) to ensure proper formatting
    try:
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    except locale.Error:
        print("Error: No se pudo establecer la configuración regional.")
    
    # Establish a connection using the connection function from 'connection.py'
    con = connection()
    if con is None:
        print("Error: No se pudo establecer la conexión con la base de datos.")
        return

    try:
        cursor = con.cursor()  # Create a cursor to interact with the database

        # Execute the SQL query to retrieve the sales data
        cursor.execute('''
            SELECT
                MAKE_DATE(EXTRACT(YEAR FROM c.registration_date)::INT, EXTRACT(MONTH FROM c.registration_date)::INT, 1) AS period,
                c.name AS name,
                c.customer_id as customers
            FROM clothing_store.customers c 
            WHERE 
                MAKE_DATE(EXTRACT(YEAR FROM c.registration_date)::INT, EXTRACT(MONTH FROM c.registration_date)::INT, 1) BETWEEN '2024-01-01' AND '2024-12-01'
            ORDER BY 
                MAKE_DATE(EXTRACT(YEAR FROM c.registration_date)::INT, EXTRACT(MONTH FROM c.registration_date)::INT, 1);;
        ''')

        records = cursor.fetchall()  # Fetch all the results

        # Convert results into a DataFrame for better visualization.
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(records, columns=columns)

        print(df)

        return df

    except psycopg2.Error as e:
        print(f"Error executing the query: {e}")
        return None

    finally:
        # Close cursor and connection safely
        cursor.close()
        con.close()
        print("Connection closed successfully.")