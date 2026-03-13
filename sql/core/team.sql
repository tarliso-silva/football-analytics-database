CREATE TABLE core.team (
    team_id BIGSERIAL PRIMARY KEY,
    team_name TEXT NOT NULL UNIQUE
);