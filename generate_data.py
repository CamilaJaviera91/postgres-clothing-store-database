from faker import Faker
import random

# Initialize the Faker library
fake = Faker()

# Set the number of entries to generate
num_entries = 500

# Generate unique IDs
unique_ids = set()
while len(unique_ids) < num_entries:
    unique_ids.add(random.randint(1000, 99999))  # Generate unique random numbers between 1000 and 99999

# Convert the unique IDs set to a list for pairing with other data
unique_ids = list(unique_ids)

# Generate the data
customers = []
for i in range(num_entries):
    customer_id = unique_ids[i]  # Unique ID
    name = fake.name().replace("'", "''")  # Escape single quotes
    email = fake.email().replace("'", "''")
    phone = fake.phone_number().replace("'", "''")
    address = fake.address().replace("\n", ", ").replace("'", "''")
    date = fake.date_between(start_date='-10y', end_date='today')  # Date in YYYY-MM-DD format
    customers.append((customer_id, name, email, phone, address, date))

# Print the data in SQL format
print("INSERT INTO clothing_store.customers (customer_id, name, email, phone, address, registration_date) VALUES")
values = ",\n".join(
    [f"    ('{c[0]}', '{c[1]}', '{c[2]}', '{c[3]}', '{c[4]}', '{c[5]}')" for c in customers]
)
print(values + ";")