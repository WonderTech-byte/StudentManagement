from datetime import datetime, timezone

from bson.errors import InvalidId
from fastapi import HTTPException, status
from pymongo.errors import DuplicateKeyError

from app import repository
from app.model import UserRole


def bad_request(message: str):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)


def not_found(message: str):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)


def conflict(message: str):
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=message)


def safe_get_user(user_id: str):
    try:
        user = repository.get_user_by_id(user_id)
    except InvalidId:
        bad_request("Invalid user id.")

    if not user:
        not_found("User not found.")

    return user


def safe_get_course(course_id: str):
    try:
        course = repository.get_course_by_id(course_id)
    except InvalidId:
        bad_request("Invalid course id.")

    if not course:
        not_found("Course not found.")

    return course


def create_user(payload):
    user_data = {
        "name": payload.name,
        "email": str(payload.email),
        "role": payload.role.value,
        "created_at": datetime.now(timezone.utc),
    }
    try:
        return repository.create_user(user_data)
    except DuplicateKeyError:
        conflict("A user with this email already exists.")


def create_course(payload):
    facilitator = safe_get_user(payload.facilitator_id)
    if facilitator["role"] != UserRole.facilitator.value:
        conflict("Only a facilitator can create a course.")

    course_data = {
        "title": payload.title,
        "description": payload.description,
        "facilitator_id": facilitator["id"],
        "created_at": datetime.now(timezone.utc),
    }
    return repository.create_course(course_data)


def get_all_courses():
    return repository.get_all_courses()


def get_course(course_id: str):
    return safe_get_course(course_id)


def enroll_student(course_id: str, student_id: str):
    safe_get_course(course_id)
    student = safe_get_user(student_id)
    if student["role"] != UserRole.student.value:
        conflict("Only a student can be enrolled in a course.")

    existing_enrollment = repository.get_enrollment_by_student_and_course(
        student_id,
        course_id,
    )
    if existing_enrollment:
        conflict("Student is already enrolled in this course.")

    enrollment_data = {
        "student_id": student_id,
        "course_id": course_id,
        "grade": None,
        "graded_at": None,
        "created_at": datetime.now(timezone.utc),
    }
    return repository.create_enrollment(enrollment_data)


def assign_grade(course_id: str, facilitator_id: str, student_id: str, grade: float):
    course = safe_get_course(course_id)
    if course["facilitator_id"] != facilitator_id:
        conflict("Only the course facilitator can assign grades.")

    enrollment = repository.get_enrollment_by_student_and_course(student_id, course_id)
    if not enrollment:
        not_found("Student is not enrolled in this course.")

    graded_at = datetime.now(timezone.utc)
    return repository.update_grade(enrollment["id"], grade, graded_at)


def get_students_in_course(course_id: str, facilitator_id: str):
    course = safe_get_course(course_id)
    if course["facilitator_id"] != facilitator_id:
        conflict("Only the course facilitator can view enrolled students.")

    enrollments = repository.get_course_enrollments(course_id)
    students = []

    for enrollment in enrollments:
        student = safe_get_user(enrollment["student_id"])
        students.append(
            {
                "student_id": student["id"],
                "student_name": student["name"],
                "student_email": student["email"],
                "enrolled_at": enrollment["created_at"],
                "grade": enrollment["grade"],
                "graded_at": enrollment["graded_at"],
            }
        )

    return students


def get_student_courses(student_id: str):
    student = safe_get_user(student_id)
    if student["role"] != UserRole.student.value:
        conflict("This user is not a student.")

    enrollments = repository.get_student_enrollments(student_id)
    courses = []

    for enrollment in enrollments:
        course = safe_get_course(enrollment["course_id"])
        facilitator = safe_get_user(course["facilitator_id"])
        courses.append(
            {
                "course_id": course["id"],
                "course_title": course["title"],
                "facilitator_id": facilitator["id"],
                "facilitator_name": facilitator["name"],
                "enrolled_at": enrollment["created_at"],
                "grade": enrollment["grade"],
                "graded_at": enrollment["graded_at"],
            }
        )

    return courses


def get_student_grades(student_id: str):
    courses = get_student_courses(student_id)
    graded_courses = []

    for course in courses:
        if course["grade"] is not None:
            graded_courses.append(course)

    return graded_courses
