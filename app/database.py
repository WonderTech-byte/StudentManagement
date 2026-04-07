from pymongo import MongoClient


MONGODB_URI = "mongodb://localhost:27017"
DATABASE_NAME = "student_course_management"

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]

users_collection = db["users"]
courses_collection = db["courses"]
enrollments_collection = db["enrollments"]
