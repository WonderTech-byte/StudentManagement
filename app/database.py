from pymongo import MongoClient


MONGODB_URI = "mongodb://localhost:27017"
DATABASE_NAME = "student_course_management"

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]

users_collection = db["users"]
courses_collection = db["courses"]
enrollments_collection = db["enrollments"]


def check_database_connection() -> None:
    client.admin.command("ping")


def create_indexes() -> None:
    users_collection.create_index("email", unique=True)
    enrollments_collection.create_index(
        [("student_id", 1), ("course_id", 1)],
        unique=True,
    )


def close_database_connection() -> None:
    client.close()
