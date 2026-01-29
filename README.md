# Energy Monitoring Data Platform

## Overview

Energy Monitoring Data Platform is a backend-focused MVP designed to simulate a real-world **data quality and API platform**.  
The project manages energy consumption data from buildings, combining **MongoDB**, **relational SQL**, and **API automation** to reflect how data systems are built and maintained in production environments.

This is not a simple CRUD application.  
The main goal is to demonstrate **data modeling**, **data quality validation**, **API design**, and **automation workflows**, closely aligned with real technical roles.

---

## Project Goals

- Manage energy consumption data from multiple buildings
- Validate and classify data quality automatically
- Expose clean and reliable APIs for data consumption
- Combine NoSQL and relational databases in a coherent architecture
- Simulate real backend responsibilities found in data-driven companies

---

## Use Case

The platform stores energy sensor data for buildings.  
Each data record represents a measurement taken at a specific moment.

Typical use cases:

- Ingest raw sensor data
- Detect invalid, incomplete, or inconsistent records
- Store raw data and validated data separately
- Provide APIs to query clean and reliable datasets
- Generate basic data quality metrics

---

## Data Model

Each energy record contains:

- `buildingId`
- `timestamp`
- `energyConsumption`
- `temperature`
- `provider`
- `dataQualityStatus`  
  - `VALID`
  - `INCOMPLETE`
  - `INCONSISTENT`

---

## Architecture

### Databases

- **MongoDB Atlas**
  - Stores raw sensor data
  - Flexible schema for ingestion
  - Suitable for high-volume, unstructured inputs

- **SQL (Supabase / PostgreSQL)**
  - Stores normalized and validated data
  - Used for reporting, analytics, and consistency
  - Enforces relational constraints

---

## Backend Stack

- Node.js
- Express
- MongoDB (Mongoose)
- PostgreSQL (Supabase)
- REST API
- Environment-based configuration
- Free-tier compatible services only

---

## Core Features (MVP)

- REST API to ingest energy data
- Automatic data quality validation rules
- Classification of records by quality status
- Storage of raw vs validated data
- API endpoints to query:
  - All records
  - Only valid records
  - Records by building and date range
- Basic error handling and input validation

---

## Data Quality Rules (Initial)

Examples:

- Missing required fields → `INCOMPLETE`
- Negative energy consumption → `INCONSISTENT`
- Valid values → `VALID`

Rules are designed to be easily extendable.

---

## Why This Project

This project is designed to demonstrate:

- Experience with **MongoDB and relational databases**
- Strong understanding of **data modeling**
- Awareness of **data quality challenges**
- Clean API design
- Realistic backend architecture
- Practical problem-solving beyond CRUD operations

---

## Project Status

🚧 MVP in active development  
The focus is correctness, clarity, and realism over feature quantity.

---

## Future Improvements

- Scheduled validation jobs (cron)
- Aggregated consumption metrics
- Data quality dashboards
- Authentication and role-based access
- Export endpoints for analytics tools

---

## License

This project is for educational and professional portfolio purposes.
