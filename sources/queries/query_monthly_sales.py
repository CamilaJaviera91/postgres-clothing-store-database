# Import the connection function from the 'connection' file
import sys
sys.path.append('./sources/connection/')

from connection import connection

# Import necessary libraries
import psycopg2
import locale
import pandas as pd

def query_monthly_sales():
    # Set the locale to Spanish (Spain) to ensure proper formatting
    try:
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    except locale.Error:
        print("Error: Could not establish the regional settings.")
    
    # Establish a connection using the connection function from 'connection.py'
    con = connection()
    if con is None:
        print("Error: Could not establish a connection to the database.")
        return

    try:
        cursor = con.cursor()  # Create a cursor to interact with the database

        # Execute the SQL query to retrieve the sales data
        cursor.execute('''
            SELECT DISTINCT
                MAKE_DATE(EXTRACT(YEAR FROM o.order_date)::INT, EXTRACT(MONTH FROM o.order_date)::INT, 1) AS period,
                SUM(od.quantity) AS total_quantity,
                SUM(od.unit_price) AS total_unit_price,
                SUM(od.quantity * od.unit_price) AS final_total
            FROM clothing_store.customers c 
                JOIN clothing_store.orders o ON c.customer_id = o.customer_id 
                JOIN clothing_store.order_details od ON o.order_id = od.order_id 
                JOIN clothing_store.products p ON od.product_id = p.product_id 
            WHERE 
                MAKE_DATE(EXTRACT(YEAR FROM o.order_date)::INT, EXTRACT(MONTH FROM o.order_date)::INT, 1) BETWEEN '2024-01-01' AND '2024-12-31'
            GROUP BY 
                period
            ORDER BY 
                period;

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