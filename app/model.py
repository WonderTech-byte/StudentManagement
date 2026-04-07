from datetime import datetime

from pydantic import BaseModel


class UserModel(BaseModel):
    id: str | None = None
    name: str
    email: str
    role: str
    created_at: datetime | None = None


class CourseModel(BaseModel):
    id: str | None = None
    title: str
    description: str
    facilitator_id: str
    created_at: datetime | None = None


class EnrollmentModel(BaseModel):
    id: str | None = None
    student_id: str
    course_id: str
    grade: float | None = None
    graded_at: datetime | None = None
    created_at: datetime | None = None
