from faker import Faker
import random

# Initialize the Faker library
fake = Faker()

# Set the number of entries to generate
num_entries = 500

# Generate unique data
unique_emails = set()
unique_phones = set()
unique_names = set()

# Function to ensure unique data generation
def get_unique_email():
    email = fake.email()
    while email in unique_emails:
        email = fake.email()
    unique_emails.add(email)
    return email

def get_unique_phone():
    # Generate a phone number in the format "584-294-7215"
    phone = f"58{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    while phone in unique_phones:
        phone = f"58{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    unique_phones.add(phone)
    return phone

def get_unique_name():
    name = fake.name()
    while name in unique_names:
        name = fake.name()
    unique_names.add(name)
    return name

# Generate customer data
customers = []
for i in range(num_entries):
    customer_id = random.randint(1000, 9999)  # Unique numeric ID
    name = get_unique_name().replace("'", "''")  # Ensure unique name and escape single quotes
    email = get_unique_email().replace("'", "''")  # Ensure unique email and escape single quotes
    phone = get_unique_phone().replace("'", "''")  # Ensure unique phone number and escape single quotes
    address = fake.address().replace("\n", ", ").replace("'", "''")  # Address doesn't need to be unique but can be formatted
    date = fake.date_between(start_date='-10y', end_date='today')  # Date within the last 10 years
    customers.append((customer_id, name, email, phone, address, date))

# Print the data in SQL format
print("INSERT INTO clothing_store.customers (id, name, email, phone, address, registration_date) VALUES")
values = ",\n".join(
    [f"    ({c[0]}, '{c[1]}', '{c[2]}', '{c[3]}', '{c[4]}', '{c[5]}')" for c in customers]
)
print(values + ";")