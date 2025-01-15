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
