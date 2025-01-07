from faker import Faker

# Initialize the Faker library
fake = Faker()

# Set the number of entries to generate
num_entries = 500

# Generate the data
customers = []
for _ in range(num_entries):
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    address = fake.address().replace('\n', ', ')
    customers.append((name, email, phone, address))

# Print the data in SQL format
print("INSERT INTO clothing_store.customers (name, email, phone, address) VALUES")
values = ",\n".join([f"    ('{c[0]}', '{c[1]}', '{c[2]}', '{c[3]}')" for c in customers])
print(values + ";")
