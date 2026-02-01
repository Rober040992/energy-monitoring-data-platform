# Energy Monitoring Data Platform

A production-grade backend MVP that demonstrates **clean architecture**, **data quality engineering**, and **testable domain logic** for energy consumption monitoring systems.

---

## Why This Project Exists

Real-world data systems face constant challenges with incoming data that is incomplete, inconsistent, or invalid. This platform addresses these challenges by:

- **Validating records** using explicit domain rules before persistence
- **Classifying data quality** as a first-class concern
- **Separating concerns** across domain, application, and infrastructure layers
- **Exposing controlled APIs** for data ingestion and validation

This is not a CRUD demo. It's a reflection of how production systems handle messy data in the real world.

---

## Architecture Principles

The platform is built on foundational software engineering principles:

**Domain-Driven Design**
- Business logic lives in the domain layer, independent of frameworks
- Entities and rules model real-world energy monitoring concepts
- No database or API coupling in core business logic

**Clean Architecture**
- Use cases orchestrate domain rules without knowing about HTTP or databases
- Infrastructure is an implementation detail that can be swapped
- Everything is testable in isolation

**Data Quality First**
- Quality validation happens at the domain level
- Invalid data is classified, not rejected silently
- Transparency into data health across the entire pipeline

---

## Data Model

Energy records contain the following attributes:

| Field | Type | Description |
|-------|------|-------------|
| `building_id` | string | Unique building identifier |
| `date` | date | Consumption measurement date |
| `consumption` | float | Energy consumption value |
| `temperature` | float | Ambient temperature reading |
| `provider` | string | Energy provider name |
| `quality_status` | enum | `VALID` / `INCOMPLETE` / `INCONSISTENT` |

Quality status is determined by domain validation rules and explicitly tracked throughout the system.

---

## Current Features

**Domain Layer**
- Energy record entities with business invariants
- Data quality validation rules
- Duplicate detection service

**Application Layer**
- Use cases for processing energy records
- Orchestration of validation and quality classification
- Exception-based error handling

**API Layer**
- FastAPI REST endpoints
- Pydantic schema validation
- Health check endpoint
- Validation endpoint (decoupled from persistence)

**Infrastructure**
- Environment-based configuration
- Free-tier friendly database setup (MongoDB Atlas, PostgreSQL/Supabase planned)
- Comprehensive test coverage with pytest

---

## Technology Stack

**Core Backend**
- Python 3.11+
- FastAPI for REST APIs
- Pydantic for data validation
- Uvicorn as ASGI server

**Data Storage** (planned)
- MongoDB Atlas for raw data ingestion
- PostgreSQL/Supabase for validated records

**Development Tools**
- pytest for testing
- python-dotenv for configuration
- Git for version control

---

## Project Structure

```
energy-monitoring-platform/
│
├── core/                          # Domain layer (framework-agnostic)
│   ├── entities/
│   │   └── energy_record.py      # Core business entities
│   ├── rules/
│   │   └── data_quality.py       # Validation rules
│   └── services/
│       └── duplicate_detector.py  # Domain services
│
├── use_cases/                     # Application layer
│   ├── process_energy_record.py  # Business workflows
│   └── run_use_case.py           # Use case orchestration
│
├── src/app/                       # Infrastructure layer
│   ├── api/
│   │   ├── routes/               # HTTP endpoints
│   │   │   ├── energy_records.py
│   │   │   └── health.py
│   │   ├── schemas/              # API contracts
│   │   │   ├── energy_record.py
│   │   │   └── quality.py
│   │   └── services/             # API-level services
│   ├── config/
│   │   └── env.py                # Environment configuration
│   └── main.py                   # Application entry point
│
└── tests/                         # Test suite
    ├── test_data_quality.py
    └── test_duplicate_detector.py
```

---

## Getting Started

**Prerequisites**
- Python 3.11 or higher
- pip package manager

**Installation**

```bash
# Clone the repository
git clone https://github.com/Rober040992/energy-monitoring-data-platform.git

cd energy-monitoring-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your configuration
```

**Running the Application**

```bash
# Start the API server
npm run dev

# Run tests
npm run test

# Run use_cases
npm run ues_cases
```

**API Documentation**

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## Design Decisions

**Why Clean Architecture?**
Separating domain logic from infrastructure makes the codebase testable, maintainable, and adaptable to changing requirements.

**Why Explicit Quality Classification?**
Instead of silently rejecting bad data, we classify and track it. This provides visibility into data pipeline health and enables downstream analysis.

**Why Use Cases?**
Use cases encapsulate business workflows, making the application layer a clear representation of what the system *does*, independent of how it does it.

**Why Framework Independence in Core?**
The domain layer contains the most valuable code—your business rules. Keeping it framework-agnostic protects this investment and enables easy testing.

---

## Roadmap

**Phase 1: MVP** (Current)
- ✅ Domain entities and validation rules
- ✅ Basic use cases
- ✅ FastAPI REST API
- ✅ Test coverage for core logic

**Phase 2: Persistence**
- MongoDB Atlas integration for raw data
- PostgreSQL/Supabase for validated records
- Repository pattern implementation
- Data migration scripts

**Phase 3: Optional/Advanced Features**
- Batch processing capabilities
- Data quality dashboards
- Automated duplicate resolution
- Real-time monitoring alerts
- Time-series analysis

**Phase 4: Production Readiness**
- Authentication and authorization
- Rate limiting
- Comprehensive logging and monitoring
- CI/CD pipeline
- Docker containerization
- API versioning

---

## Contributing

This project follows clean architecture principles and emphasizes testability. When contributing:

1. Keep domain logic pure and framework-independent
2. Write tests for all business rules
3. Use dependency injection for infrastructure concerns
4. Follow existing code organization patterns
5. Update documentation for architectural decisions

---

## License

[MIT]

---

## Contact

- Email: rgfrasta@gmail.com
- Linkedin: https://www.linkedin.com/in/roberto-gomez-fabrega-5a694516a/
- Github: https://github.com/Rober040992

Developed by Roberto Gomez Fabrega