-- ---------------------------------------------------------
-- LOAD COUNTRY DIMENSION
-- ---------------------------------------------------------

INSERT INTO core.country (country_name)

SELECT DISTINCT country
FROM staging.football_data_matches;



-- ---------------------------------------------------------
-- LOAD COMPETITION DIMENSION
-- ---------------------------------------------------------

INSERT INTO core.competition (competition_name, country_id)

SELECT DISTINCT
    s.league,
    c.country_id

FROM staging.football_data_matches s

JOIN core.country c
    ON c.country_name = s.country;



-- ---------------------------------------------------------
-- LOAD SEASON DIMENSION
-- ---------------------------------------------------------

INSERT INTO core.season (competition_id, season_year)

SELECT DISTINCT
    c.competition_id,
    s.season::INTEGER

FROM staging.football_data_matches s

JOIN core.competition c
    ON c.competition_name = s.league;