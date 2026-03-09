# Data Model

This document describes the conceptual data model of the Football Analytics Database.

The goal of this model is to represent football competitions, teams, seasons, and matches in a normalized relational structure.

---

# Entities

## Country

Represents the country where a competition takes place.

Attributes:

* country_id
* country_name

Example:

Brazil

---

## Competition

Represents a football competition or league.

Examples:

* Brazilian Serie A
* Premier League
* La Liga

Attributes:

* competition_id
* competition_name
* country_id

Relationship:

Competition belongs to one Country.

---

## Season

Represents a specific season of a competition.

Examples:

* 2021
* 2022
* 2023

Attributes:

* season_id
* competition_id
* season_year

Relationship:

Season belongs to one Competition.

---

## Team

Represents a football club.

Examples:

* Flamengo
* Palmeiras
* São Paulo
* Corinthians

Attributes:

* team_id
* team_name

---

## Match

Represents a football match between two teams.

Attributes:

* match_id
* season_id
* match_date
* match_time
* home_team_id
* away_team_id
* home_goals
* away_goals
* result

Relationships:

* Match belongs to one Season
* Match has one home team
* Match has one away team

---

# Entity Relationships

Country
↓
Competition
↓
Season
↓
Match

Team participates in matches as:

* home team
* away team

---

# Model Characteristics

The model follows relational design principles:

* normalized structure
* separation of entities
* use of surrogate keys

This structure supports analytical queries such as:

* head-to-head statistics
* goals per season
* team performance analysis
