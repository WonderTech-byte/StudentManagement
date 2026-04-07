from datetime import datetime

from pydantic import BaseModel


class UserModel(BaseModel):
    id: str
    name: str
    email: str
    role: str
    created_at: datetime


class CourseModel(BaseModel):
    id: str
    title: str
    description: str
    facilitator_id: str
    created_at: datetime


class EnrollmentModel(BaseModel):
    id: str
    student_id: str
    course_id: str
    grade: float | None = None
    created_at: datetime
