Fixed README.md
markdown
# University Database Management System

## ER Diagram 

```mermaid
erDiagram
    STUDENT ||--o{ ENROLLMENT : enrolls
    LECTURER ||--o{ SUBJECT : teaches
    LECTURER ||--o{ LECTURE : conducts
    SUBJECT ||--o{ ENROLLMENT : has
    SUBJECT ||--o{ LECTURE : offers

    STUDENT {
        string id PK
        string first_name
        string last_name
        string student_code UK
        string national_id UK
        date date_of_birth
        date date_of_enrolment
        string email UK
        string phone
        string address
        datetime created_at
        datetime updated_at
    }

    LECTURER {
        string id PK
        string first_name
        string last_name
        string lecturer_code UK
        string email UK
        string phone
        string address
        string department
        date hire_date
        string specialization
        datetime created_at
        datetime updated_at
    }

    SUBJECT {
        string id PK
        string subject_code UK
        string subject_name
        int units
        text description
        string level
        int max_students
        string lecturer_id FK
        datetime created_at
        datetime updated_at
    }

    ENROLLMENT {
        string id PK
        string student_id FK
        string subject_id FK
        date enrollment_date
        enum status
        string semester
        int year
        string grade
        int grade_points
        int attendance_percentage
        datetime created_at
        datetime updated_at
    }

    LECTURE {
        string id PK
        string subject_id FK
        string lecturer_id FK
        string lecture_code UK
        string lecture_name
        date lecture_date
        time start_time
        time end_time
        string day_of_week
        string room
        string building
        int capacity
        datetime created_at
        datetime updated_at
    }
```

## Relationships

| Relationship | Type | Description |
|---|---|---|
| STUDENT → ENROLLMENT | One-to-Many | One student can enroll in many subjects |
| SUBJECT → ENROLLMENT | One-to-Many | One subject can have many students |
| LECTURER → SUBJECT | One-to-Many | One lecturer can teach many subjects |
| SUBJECT → LECTURE | One-to-Many | One subject can have many lectures |
| LECTURER → LECTURE | One-to-Many | One lecturer can conduct many lectures |

# Create a venv instead
python3 -m venv .venv 
source .venv/bin/activate

# 1. Clean everything
docker compose down -v
rm -rf src/migrations/versions/*.py 

# 2. Commands
```
python src/seed.py
python src/main.py
docker compose down -v	   Remove Docker container and data
rm -rf src/migrations/versions/*.py	Delete migration files
docker compose up -d postgres	Start PostgreSQL
alembic revision --autogenerate -m "Initial migration"	Create migration
alembic upgrade head	Apply migration
python src/seed.py	Seed database
python src/main.py	Run queries