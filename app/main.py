from fastapi import FastAPI, Query, status

from app.schemas import (
    CourseCreate,
    CourseResponse,
    CourseStudentView,
    EnrollmentCreate,
    EnrollmentResponse,
    GradeAssign,
    StudentCourseView,
    UserCreate,
    UserResponse,
)
from app.services import (
    assign_grade as assign_grade_service,
    create_course as create_course_service,
    create_user as create_user_service,
    enroll_student as enroll_student_service,
    get_all_courses as get_all_courses_service,
    get_course as get_course_service,
    get_student_courses as get_student_courses_service,
    get_student_grades as get_student_grades_service,
    get_students_in_course as get_students_in_course_service,
)

app = FastAPI(title="Student Course Management System")


@app.post("/api/v1/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate):
    return create_user_service(payload)


@app.get("/api/v1/users/{student_id}/courses", response_model=list[StudentCourseView])
def get_student_courses(student_id: str):
    return get_student_courses_service(student_id)


@app.get("/api/v1/users/{student_id}/grades", response_model=list[StudentCourseView])
def get_student_grades(student_id: str):
    return get_student_grades_service(student_id)


@app.post("/api/v1/courses", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(payload: CourseCreate):
    return create_course_service(payload)


@app.get("/api/v1/courses", response_model=list[CourseResponse])
def get_all_courses():
    return get_all_courses_service()


@app.get("/api/v1/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: str):
    return get_course_service(course_id)


@app.post(
    "/api/v1/courses/{course_id}/enrollments",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
)
def enroll_student(course_id: str, payload: EnrollmentCreate):
    return enroll_student_service(course_id, payload.student_id)


@app.get("/api/v1/courses/{course_id}/students", response_model=list[CourseStudentView])
def get_students_in_course(course_id: str, facilitator_id: str = Query(...)):
    return get_students_in_course_service(course_id, facilitator_id)


@app.post("/api/v1/courses/{course_id}/grades", response_model=EnrollmentResponse)
def assign_grade(course_id: str, payload: GradeAssign, facilitator_id: str = Query(...)):
    return assign_grade_service(course_id, facilitator_id, payload.student_id, payload.grade)
