from bson import ObjectId

from app.database import courses_collection, enrollments_collection, users_collection


def to_object_id(item_id: str) -> ObjectId:
    return ObjectId(item_id)


def format_document(document: dict | None) -> dict | None:
    if not document:
        return None

    new_document = dict(document)
    new_document["id"] = str(new_document.pop("_id"))
    return new_document


def create_user(data: dict):
    result = users_collection.insert_one(data)
    return get_user_by_id(str(result.inserted_id))


def get_user_by_id(user_id: str):
    user = users_collection.find_one({"_id": to_object_id(user_id)})
    return format_document(user)


def create_course(data: dict):
    result = courses_collection.insert_one(data)
    return get_course_by_id(str(result.inserted_id))


def get_course_by_id(course_id: str):
    course = courses_collection.find_one({"_id": to_object_id(course_id)})
    return format_document(course)


def get_all_courses():
    courses = courses_collection.find().sort("created_at", -1)
    return [format_document(course) for course in courses]


def create_enrollment(data: dict):
    result = enrollments_collection.insert_one(data)
    return get_enrollment_by_id(str(result.inserted_id))


def get_enrollment_by_id(enrollment_id: str):
    enrollment = enrollments_collection.find_one({"_id": to_object_id(enrollment_id)})
    return format_document(enrollment)


def get_enrollment_by_student_and_course(student_id: str, course_id: str):
    enrollment = enrollments_collection.find_one(
        {"student_id": student_id, "course_id": course_id}
    )
    return format_document(enrollment)


def update_grade(enrollment_id: str, grade: float, graded_at):
    enrollments_collection.update_one(
        {"_id": to_object_id(enrollment_id)},
        {"$set": {"grade": grade, "graded_at": graded_at}},
    )
    return get_enrollment_by_id(enrollment_id)


def get_course_enrollments(course_id: str):
    enrollments = enrollments_collection.find({"course_id": course_id})
    return [format_document(enrollment) for enrollment in enrollments]


def get_student_enrollments(student_id: str):
    enrollments = enrollments_collection.find({"student_id": student_id})
    return [format_document(enrollment) for enrollment in enrollments]
