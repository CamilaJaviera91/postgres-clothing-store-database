from faker import Faker
import random

# Initialize the Faker library
fake = Faker()

# Set the number of entries to generate
num_entries = 500

# Data storage for uniqueness checks
unique_ids = set()
unique_names = set()
unique_emails = set()
unique_phones = set()
unique_addresses = set()
unique_dates = set()

# Function to generate a unique ID
def get_unique_id():
    unique_id = random.randint(1000, 9999)
    while unique_id in unique_ids:
        unique_id = random.randint(1000, 9999)
    unique_ids.add(unique_id)
    return unique_id

# Function to generate a unique name
def get_unique_name():
    name = fake.name()
    while name in unique_names:
        name = fake.name()
    unique_names.add(name)
    return name.replace("'", "''")  # Escape single quotes

# Function to generate a unique email
def get_unique_email():
    email = fake.email()
    while email in unique_emails:
        email = fake.email()
    unique_emails.add(email)
    return email.replace("'", "''")  # Escape single quotes

# Function to generate a unique phone number
def get_unique_phone():
    phone = f"58{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    while phone in unique_phones:
        phone = f"58{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    unique_phones.add(phone)
    return phone

# Function to generate a unique address
def get_unique_address():
    address = fake.address().replace("\n", ", ")
    while address in unique_addresses:
        address = fake.address().replace("\n", ", ")
    unique_addresses.add(address)
    return address.replace("'", "''")  # Escape single quotes

# Function to generate a unique registration date
def get_unique_date():
    date = fake.date_between(start_date='-10y', end_date='today')
    while date in unique_dates:
        date = fake.date_between(start_date='-10y', end_date='today')
    unique_dates.add(date)
    return date

# Generate customer data
customers = []
for _ in range(num_entries):
    customer_id = get_unique_id()
    name = get_unique_name()
    email = get_unique_email()
    phone = get_unique_phone()
    address = get_unique_address()
    date = get_unique_date()
    customers.append((customer_id, name, email, phone, address, date))

# Print the data in SQL format
print("INSERT INTO clothing_store.customers (customer_id, name, email, phone, address, registration_date) VALUES")
values = ",\n".join(
    [f"    ({c[0]}, '{c[1]}', '{c[2]}', '{c[3]}', '{c[4]}', '{c[5]}')" for c in customers]
)
print(values + ";")