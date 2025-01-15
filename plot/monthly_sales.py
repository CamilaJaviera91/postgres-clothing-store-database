# Import necessary libraries
import matplotlib.pyplot as plt
import sys
import pandas as pd
sys.path.append('./sources/queries/')

# Import dataframe from "query_monthly_sales"
from query_monthly_sales import query_monthly_sales as qms

# Create dataframe
df = qms()

# Convert 'period' to datetime if it's a date
df['period'] = pd.to_datetime(df['period'])

# Select the fields that we are going to use
period = df['period']
final_total = df['final_total']

# Plot the graph
plt.figure(figsize=(10, 6))
plt.bar(period, final_total, color="lightgreen")

plt.title('Period vs Total Sales')
plt.xlabel('Period')
plt.ylabel('Total Sales')
plt.xticks(rotation=45) 

# Etiquetas sobre cada barra
for x, y in zip(period, final_total):
    plt.text(x, y + 5, str(round(y, 2)), ha='center', va='bottom', fontsize=8)

plt.tight_layout()  # Ajusta el gráfico para evitar que se corte
plt.show()
