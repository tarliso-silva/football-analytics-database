CREATE TABLE core.match (
    match_id BIGSERIAL PRIMARY KEY,
    season_id BIGINT NOT NULL,
    match_date DATE NOT NULL,
    match_time TIME,
    home_team_id BIGINT NOT NULL,
    away_team_id BIGINT NOT NULL,
    home_goals INTEGER,
    away_goals INTEGER,

    CONSTRAINT fk_match_season
        FOREIGN KEY (season_id)
        REFERENCES core.season(season_id),

    CONSTRAINT fk_match_home_team
        FOREIGN KEY (home_team_id)
        REFERENCES core.team(team_id),

    CONSTRAINT fk_match_away_team
        FOREIGN KEY (away_team_id)
        REFERENCES core.team(team_id),

    CONSTRAINT chk_teams_different
        CHECK (home_team_id <> away_team_id)
);