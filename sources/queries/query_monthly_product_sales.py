# Import the connection function from the 'connection' file
import sys
sys.path.append('./sources/connection/')

from connection import connection

# Import necessary libraries
import psycopg2
import locale
import pandas as pd

def query_monthly_product_sales():
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
            SELECT distinct
                p.name,
                EXTRACT(YEAR FROM o.order_date) AS year,
                EXTRACT(MONTH FROM o.order_date) AS month,
                SUM(od.quantity) AS total_quantity,
                SUM(od.unit_price) AS total_unit_price,
                SUM(od.quantity * od.unit_price) AS final_total
            FROM clothing_store.customers c 
            JOIN clothing_store.orders o ON c.customer_id = o.customer_id 
            JOIN clothing_store.order_details od ON o.order_id = od.order_id 
            JOIN clothing_store.products p ON od.product_id = p.product_id 
            GROUP BY 
                EXTRACT(YEAR FROM o.order_date),
                EXTRACT(MONTH FROM o.order_date),
                p.name
            ORDER BY 
                EXTRACT(YEAR FROM o.order_date),
                EXTRACT(MONTH FROM o.order_date);
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