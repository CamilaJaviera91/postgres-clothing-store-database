ALTER TABLE clothing_store.customers ALTER COLUMN customer_id TYPE text USING customer_id::text;
ALTER TABLE clothing_store.customers ALTER COLUMN "name" TYPE varchar USING "name"::varchar;
ALTER TABLE clothing_store.customers ALTER COLUMN phone TYPE varchar USING phone::varchar;
ALTER TABLE clothing_store.customers ALTER COLUMN email TYPE varchar USING email::varchar;
