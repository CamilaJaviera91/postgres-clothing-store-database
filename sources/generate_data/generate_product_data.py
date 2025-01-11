from faker import Faker
import random

# Initialize the Faker library
fake = Faker()

# Set the number of entries to generate
num_entries = 100

# List of predefined categories
categories = ["Clothing", "Footwear", "Accessories", "Outerwear", "Activewear"]

# Generate unique data in advance
unique_ids = random.sample(range(1000, 9999), num_entries)  # Pre-generate unique IDs
unique_names = [fake.unique.word().capitalize() + " " + fake.word().capitalize() for _ in range(num_entries)]
unique_prices = [round(random.uniform(10, 500), 2) for _ in range(num_entries)]
unique_stocks = random.sample(range(1, 1000), num_entries)  # Pre-generate unique stock values
unique_categories = [random.choice(categories) for _ in range(num_entries)]

# Combine the data into products
products = [
    (unique_ids[i], unique_names[i], unique_prices[i], unique_stocks[i], unique_categories[i])
    for i in range(num_entries)
]

# Print the data in SQL format
print("INSERT INTO clothing_store.products (product_id, name, price, stock, category) VALUES")
values = ",\n".join(
    [f"    ({p[0]}, '{p[1]}', {p[2]}, {p[3]}, '{p[4]}')" for p in products]
)
print(values + ";")
