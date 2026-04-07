from datetime import datetime

from pydantic import BaseModel, Field





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
