from fastapi import FastAPI

from app.routers.courses import router as courses_router
from app.routers.enrollments import router as enrollments_router
from app.routers.users import router as users_router

app = FastAPI(title="Student Course Management System")

app.include_router(users_router)
app.include_router(courses_router)
app.include_router(enrollments_router)


@app.get("/")
def read_root():
    return {"message": "Student Course Management API"}
