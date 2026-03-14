-- ---------------------------------------------------------
-- LOAD COUNTRY DIMENSION
-- ---------------------------------------------------------

INSERT INTO core.country (country_name)

SELECT DISTINCT country
FROM staging.football_data_matches;