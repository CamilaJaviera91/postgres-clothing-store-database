ALTER TABLE clothing_store.orders ALTER COLUMN order_date TYPE date USING order_date::date;
