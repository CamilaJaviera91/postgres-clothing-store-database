# Import necessary libraries
import matplotlib.pyplot as plt
import sys
import pandas as pd
sys.path.append('./sources/queries/')

# Import dataframe from "query_monthly_product_sales"
from query_monthly_product_sales import query_monthly_product_sales as qmps

# Create dataframe
# Retrieves monthly product sales
df = qmps()

# Select the fields that we are going to use
# Extracts 'product' and 'final_total' columns for visualization
product = df['product']
final_total = df['final_total']

# Plot the graph
plt.figure(figsize=(10, 6))  # Sets the figure size
plt.bar(product, final_total, color="lightgreen")  # Creates a bar plot

plt.title('(Top 10) Products vs Total Sales')  # Sets the plot title
plt.xlabel('Products')  # Labels the x-axis
plt.ylabel('Total Sales')  # Labels the y-axis
plt.xticks(rotation=45)  # Rotates x-axis labels for better readability

# Labels on top of each bar
# Displays the exact sales value above each bar
for x, y in zip(product, final_total):
    plt.text(x, y + 5, str(round(y, 2)), ha='center', va='bottom', fontsize=8)

plt.tight_layout()  # Adjusts layout to prevent clipping
plt.show()  # Displays the plot

# Print all periods for verification
print("All products in the dataset:")
print(product)