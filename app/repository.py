from bson import ObjectId

from app.database import courses_collection, enrollments_collection, users_collection


def create_user(data: dict):
    result = users_collection.insert_one(data)
    return get_user_by_id(str(result.inserted_id))


def get_user_by_id(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        return None

    user["id"] = str(user["_id"])
    del user["_id"]
    return user


def create_course(data: dict):
    result = courses_collection.insert_one(data)
    return get_course_by_id(str(result.inserted_id))


def get_course_by_id(course_id: str):
    course = courses_collection.find_one({"_id": ObjectId(course_id)})
    if not course:
        return None

    course["id"] = str(course["_id"])
    del course["_id"]
    return course


def get_all_courses():
    courses = courses_collection.find().sort("created_at", -1)
    course_list = []

    for course in courses:
        course["id"] = str(course["_id"])
        del course["_id"]
        course_list.append(course)

    return course_list


def create_enrollment(data: dict):
    result = enrollments_collection.insert_one(data)
    return get_enrollment_by_id(str(result.inserted_id))


def get_enrollment_by_id(enrollment_id: str):
    enrollment = enrollments_collection.find_one({"_id": ObjectId(enrollment_id)})
    if not enrollment:
        return None

    enrollment["id"] = str(enrollment["_id"])
    del enrollment["_id"]
    return enrollment


def get_enrollment_by_student_and_course(student_id: str, course_id: str):
    enrollment = enrollments_collection.find_one(
        {"student_id": student_id, "course_id": course_id}
    )
    if not enrollment:
        return None

    enrollment["id"] = str(enrollment["_id"])
    del enrollment["_id"]
    return enrollment


def update_grade(enrollment_id: str, grade: float, graded_at):
    enrollments_collection.update_one(
        {"_id": ObjectId(enrollment_id)},
        {"$set": {"grade": grade, "graded_at": graded_at}},
    )
    return get_enrollment_by_id(enrollment_id)


def get_course_enrollments(course_id: str):
    enrollments = enrollments_collection.find({"course_id": course_id})
    enrollment_list = []

    for enrollment in enrollments:
        enrollment["id"] = str(enrollment["_id"])
        del enrollment["_id"]
        enrollment_list.append(enrollment)

    return enrollment_list


def get_student_enrollments(student_id: str):
    enrollments = enrollments_collection.find({"student_id": student_id})
    enrollment_list = []

    for enrollment in enrollments:
        enrollment["id"] = str(enrollment["_id"])
        del enrollment["_id"]
        enrollment_list.append(enrollment)

    return enrollment_list
