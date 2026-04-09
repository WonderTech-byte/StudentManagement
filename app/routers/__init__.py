from app.routers.courses import router as courses_router
from app.routers.enrollments import router as enrollments_router
from app.routers.users import router as users_router

__all__ = ["users_router", "courses_router", "enrollments_router"]
