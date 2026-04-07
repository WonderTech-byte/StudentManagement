from datetime import datetime

from pydantic import BaseModel, Field

from app.model import CourseModel, EnrollmentModel, UserModel


class UserCreate(BaseModel):
    name: str
    email: str
    role: str


class UserResponse(UserModel):
    pass


class CourseCreate(BaseModel):
    title: str
    description: str
    facilitator_id: str


class CourseResponse(CourseModel):
    pass


class EnrollmentCreate(BaseModel):
    student_id: str


class EnrollmentResponse(EnrollmentModel):
    pass


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


class CourseStudentView(BaseModel):
    student_id: str
    student_name: str
    student_email: str
    enrolled_at: datetime | None = None
    grade: float | None = None
