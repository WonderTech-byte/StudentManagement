from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class UserRole(str, Enum):
    student = "student"
    facilitator = "facilitator"


class UserBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    role: UserRole


class UserModel(UserBase):
    id: str
    created_at: datetime


class CourseBase(BaseModel):
    title: str = Field(min_length=2, max_length=120)
    description: str = Field(min_length=10, max_length=1000)
    facilitator_id: str


class CourseModel(CourseBase):
    id: str
    created_at: datetime


class EnrollmentBase(BaseModel):
    student_id: str
    course_id: str


class EnrollmentModel(EnrollmentBase):
    id: str
    grade: float | None = None
    graded_at: datetime | None = None
    created_at: datetime
