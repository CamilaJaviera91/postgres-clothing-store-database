# Import necessary libraries
import matplotlib.pyplot as plt
import sys
import pandas as pd
sys.path.append('./sources/queries/')

# Import dataframe from "query_monthly_sales"
from query_monthly_sales import query_monthly_sales as qms

# Create dataframe
# Retrieves monthly sales data
df = qms()

# Convert 'period' to datetime if it's a date
# Ensures the 'period' column is in datetime format for proper plotting
df['period'] = pd.to_datetime(df['period'])

# Select the fields that we are going to use
# Extracts 'period' and 'final_total' columns for visualization
period = df['period']
final_total = df['final_total']

# Plot the graph
plt.figure(figsize=(10, 6))  # Sets the figure size
plt.bar(period, final_total, color="darkred", width=20)  # Creates a bar plot

plt.title('Period vs Total Sales')  # Sets the plot title
plt.xlabel('Period')  # Labels the x-axis
plt.ylabel('Total Sales')  # Labels the y-axis
plt.xticks(period[::len(period)//12], rotation=90)  # Muestra 12 etiquetas espaciadas uniformemente

# Labels on top of each bar
# Displays the exact sales value above each bar
for x, y in zip(period, final_total):
    plt.text(x, y + 5, str(round(y, 2)), ha='center', va='bottom', fontsize=8)

plt.tight_layout()  # Adjusts layout to prevent clipping
plt.show()  # Displays the plot

# Print all periods for verification
print("All periods in the dataset:")
print(period)
