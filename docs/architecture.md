# Football Analytics Database Architecture

## Project Overview

This project aims to build a relational database for football analytics using public datasets.

The database is designed to support complex statistical queries about football matches, teams, and competitions.

Examples of questions the database should answer:

* How many matches have two teams played against each other?
* Which player has received the most red cards in a competition?
* Average goals per season
* Historical head-to-head statistics
* Team disciplinary records

---

## Technology Stack

Database
PostgreSQL

ETL
Python

Query Language
SQL

Visualization
Power BI

---

## Data Architecture

The database is organized into logical schemas.

### staging

Stores raw data exactly as received from external datasets.

Purpose:

* auditability
* ETL processing
* data traceability

Examples:

staging.football_data_matches

---

### core

Main relational model of the database.

Contains normalized football entities.

Examples:

* competition
* season
* team
* player
* match
* match_event

---

### reference

Stores domain reference tables and controlled vocabularies.

Examples:

* country
* confederation
* competition_type
* event_type

---

### analytics

Contains analytical views and derived datasets.

Examples:

* head_to_head
* team_statistics
* goal_statistics
* card_statistics

---

## Data Pipeline

External datasets
↓
staging schema
↓
ETL transformations
↓
core schema
↓
analytics views
↓
Dashboards and analytical queries

---

## Initial Dataset

The first dataset used in this project will be:

Football-Data.co.uk

Reason:

* simple structure
* historical match data
* suitable for initial database modeling
