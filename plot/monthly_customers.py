# Import necessary libraries
import matplotlib.pyplot as plt
import sys
import pandas as pd
sys.path.append('./sources/queries/')

# Import dataframe from "query_customers"
from query_customers import query_customers as qc

# Create dataframe
# Retrieves "query_customers" data
df = qc()

# Convert 'period' to datetime if it's a date
df['period'] = pd.to_datetime(df['period'])

# Ensure 'customers' has valid numeric data
df['customers'] = df['customers'].nunique()

# Select the fields that we are going to use
period = df['period']
customers = df['customers'] 

# Plot the graph
plt.figure(figsize=(10, 6))
plt.bar(period, customers, color="darkred", width=15)  # Adjusted width

plt.title('Period vs Total Customers')  # Corrected title
plt.xlabel('Period')
plt.ylabel('Total Customers')  # Corrected label

# Adjust x-ticks to show 12 values or less
plt.xticks(period[::len(period)%12], rotation=90)  # Muestra 12 etiquetas espaciadas uniformemente

# Labels on top of each bar
for x, y in zip(period, customers):
    plt.text(x, y , str(round(y, 2)), ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()

# Print all periods for verification
print("All periods in the dataset:")
print(period)
