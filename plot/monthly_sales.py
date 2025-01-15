# Import necessary libraries
import matplotlib.pyplot as plt
import sys
import pandas as pd
sys.path.append('./sources/queries/')

# Import dataframe from "query_monthly_sales"
from query_monthly_sales import  query_monthly_sales as qms

# Create dataframe
df = qms()

# Select the fields that we are going to use
period = df['period']
final_total = df['final_total']

# Plot the graph

plt.bar(period, final_total, color="Lightgreen")

plt.title('Period vs Total Sales')
plt.xlabel('Period')
plt.ylabel('Total')

# Etiquetas sobre cada barra
for i, value in enumerate(final_total):
    plt.text(i, value + 5, str(value), ha='center')

plt.show()