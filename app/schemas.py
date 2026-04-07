from datetime import datetime

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str
    email: str
    role: str


class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    role: str
    created_at: datetime


class CourseCreate(BaseModel):
    title: str
    description: str
    facilitator_id: str


class CourseResponse(BaseModel):
    id: str
    title: str
    description: str
    facilitator_id: str
    created_at: datetime


class EnrollmentCreate(BaseModel):
    student_id: str


class EnrollmentResponse(BaseModel):
    id: str
    student_id: str
    course_id: str
    grade: float | None = None
    graded_at: datetime | None = None
    created_at: datetime


class GradeAssign(BaseModel):
    student_id: str
    grade: float = Field(ge=0, le=100)


class StudentCourseView(BaseModel):
    course_id: str
    course_title: str
    facilitator_id: str
    facilitator_name: str
    enrolled_at: datetime | None = None
    grade: float | None = None
    graded_at: datetime | None = None


class CourseStudentView(BaseModel):
    student_id: str
    student_name: str
    student_email: str
    enrolled_at: datetime | None = None
    grade: float | None = None
    graded_at: datetime | None = None
