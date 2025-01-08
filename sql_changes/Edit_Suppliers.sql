ALTER TABLE clothing_store.suppliers ALTER COLUMN "name" TYPE varchar USING "name"::varchar;
ALTER TABLE clothing_store.suppliers ALTER COLUMN phone TYPE varchar USING phone::varchar;
ALTER TABLE clothing_store.suppliers ALTER COLUMN email TYPE varchar USING email::varchar;
ALTER TABLE clothing_store.suppliers ALTER COLUMN address TYPE varchar USING address::varchar;
