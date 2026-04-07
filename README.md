# Student Course Management System

RESTful API for managing students, facilitators, courses, enrollments, and grades with FastAPI and MongoDB.

## Features

- Create `student` and `facilitator` users
- Create and retrieve courses
- Enroll students in courses
- Assign grades only to enrolled students
- View a student's enrolled courses and graded courses
- View students enrolled in a facilitator's course

## Project Structure

```text
app/
  main.py             FastAPI endpoints
  database.py         MongoDB connection
  schemas.py          request and response models
  repository.py       database operations
  services.py         business logic
docs/                 UML diagrams
```

## Setup

1. Create a virtual environment and install dependencies.
2. Copy `.env.example` to `.env`.
3. Ensure MongoDB is running locally or update `MONGODB_URI`.
4. Start the API:

```bash
uvicorn app.main:app --reload
```

Swagger UI will be available at `http://127.0.0.1:8000/docs`.

## API Summary

- `POST /api/v1/users`
- `GET /api/v1/users/{student_id}/courses`
- `GET /api/v1/users/{student_id}/grades`
- `POST /api/v1/courses`
- `GET /api/v1/courses`
- `GET /api/v1/courses/{course_id}`
- `POST /api/v1/courses/{course_id}/enrollments`
- `GET /api/v1/courses/{course_id}/students?facilitator_id=...`
- `POST /api/v1/courses/{course_id}/grades?facilitator_id=...`

## UML Artifacts

- Class diagram: `docs/class-diagram.puml`
- Use case diagram: `docs/use-case-diagram.puml`
