CREATE TABLE core.season (
    season_id BIGSERIAL PRIMARY KEY,
    competition_id BIGINT NOT NULL,
    season_year INTEGER NOT NULL,

    CONSTRAINT fk_season_competition
        FOREIGN KEY (competition_id)
        REFERENCES core.competition(competition_id),

    CONSTRAINT uq_season_competition_year
        UNIQUE (competition_id, season_year)
);