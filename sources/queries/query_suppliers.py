# Import the connection function from the 'connection' file
import sys
sys.path.append('./sources/connection/')

from connection import connection

# Import necessary libraries
import psycopg2
import locale
import pandas as pd

def query_suppliers():
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
                s.supplier_id,
                s.name AS supplier_name,
                p.product_id,
                p.name AS product_name,
                ps.purchase_price,
                ps.last_updated,
                EXTRACT(YEAR FROM ps.last_updated) as year,
                EXTRACT(MONTH FROM ps.last_updated) as month
            FROM clothing_store.products_suppliers ps
            JOIN clothing_store.products p ON ps.product_id = p.product_id 
            JOIN clothing_store.suppliers s ON ps.supplier_id = s.supplier_id
            ORDER BY last_updated;
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