from faker import Faker
import random

# Initialize the Faker library
fake = Faker()

# Set the number of entries to generate
num_entries = 50

"""
Extract suppliers id with the sentence
select s.supplier_id  from clothing_store.suppliers s  
"""
suppliers_ids = [3880,	4100,	7928,	8284,	7362,	9306,	1473,	4629,	6074,	1383,	
                8356,	6422,	3379,	7328,	1450,	9614,	9588,	6040,	9447,	7441,	
                6284,	8605,	8355,	8316,	1124,	5390,	2149,	6574,	1607,	7936,	
                2380,	8222,	1468,	9646,	9795,	8037,	7670,	2101,	2082,	3734,	
                2253,	6447,	3905,	5614,	9523,	6380,	3688,	2308,	9867,	8884]

"""
Extract product_id with the sentence
select p.product_id  from clothing_store.products p 
"""
products_ids = [6774,	1823,	9967,	8773,	3282,	7690,	7192,	6505,	3340,	8987,	
                9390,	3572,	4464,	2141,	5265,	5196,	6030,	9739,	4177,	8421,	
                1460,	1681,	4738,	6314,	4554,	8313,	5636,	9576,	9771,	9411,	
                5045,	1483,	6458,	8448,	7422,	9626,	1854,	5517,	6015,	5258,	
                1510,	2381,	6039,	9327,	6803,	6923,	3371,	9432,	2608,	9630,	
                6331,	3576,	3643,	9528,	6910,	7667,	2637,	8659,	3218,	7216,	
                3548,	6897,	8395,	8294,	7500,	2276,	2892,	1609,	6943,	5015,	
                4042,	9895,	9921,	2499,	7695,	4466,	1728,	8735,	9192,	2564,	
                8358,	7243,	9904,	9814,	3164,	3780,	9357,	8413,	3972,	4619,	
                5829,	2569,	8461,	9600,	3817,	1716,	3123,	3949,	2800,	2740]

# Generate unique data in advance
unique_suppliers_ids = [random.choice(suppliers_ids) for _ in range(num_entries)]
unique_products_ids = [random.choice(products_ids) for _ in range(num_entries)]
unique_purchases_price = random.sample(range(1000, 9999), num_entries)
last_update = [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_entries)]

# Combine the data into products
products = [
    (unique_suppliers_ids[i], unique_products_ids[i], unique_purchases_price[i], last_update[i])
    for i in range(num_entries)
]

# Print the data in SQL format
print("INSERT INTO clothing_store.products_suppliers (supplier_id, product_id, purchase_price, last_updated) VALUES")
values = ",\n".join(
    [f"    ({p[0]}, {p[1]}, {p[2]}, '{p[3]}')" for p in products]
)
print(values + ";")
