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



-- ---------------------------------------------------------
-- LOAD TEAM DIMENSION
-- ---------------------------------------------------------

INSERT INTO core.team (team_name)

SELECT DISTINCT home
FROM staging.football_data_matches

UNION

SELECT DISTINCT away
FROM staging.football_data_matches;



-- ---------------------------------------------------------
-- LOAD MATCH FACT TABLE
-- ---------------------------------------------------------

INSERT INTO core.match (
    season_id,
    match_date,
    match_time,
    home_team_id,
    away_team_id,
    home_goals,
    away_goals
)

SELECT
    s2.season_id,
    TO_DATE(s.date, 'DD/MM/YYYY'),
    s.time::TIME,
    ht.team_id,
    at.team_id,
    s.hg::INTEGER,
    s.ag::INTEGER

FROM staging.football_data_matches s

JOIN core.season s2
    ON s2.season_year = s.season::INTEGER

JOIN core.team ht
    ON ht.team_name = s.home

JOIN core.team at
    ON at.team_name = s.away;