# Project Decision Log

This document records important technical decisions made during the development of the Football Analytics Database.

The goal is to keep a clear history of architectural and data engineering choices.

---

## 2026-03-05

### Decision

Use **Football-Data.co.uk** as the initial dataset for the project.

### Reason

* Simple CSV structure
* Easy to ingest
* Provides historical match data
* Ideal for building the first version of the relational model

### Impact

The first version of the database will focus on:

* competitions
* seasons
* teams
* matches
* goals
* cards

More detailed event data may be added later using other datasets such as StatsBomb.
