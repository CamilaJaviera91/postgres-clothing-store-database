ALTER TABLE clothing_store.customers ALTER COLUMN "name" TYPE varchar USING "name"::varchar;
ALTER TABLE clothing_store.customers ALTER COLUMN email TYPE varchar USING email::varchar;
ALTER TABLE clothing_store.customers ALTER COLUMN phone TYPE varchar USING phone::varchar;
ALTER TABLE clothing_store.customers ALTER COLUMN address TYPE varchar USING address::varchar;
