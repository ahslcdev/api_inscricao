from fastapi import FastAPI
from app.enrollment_api.routes.enrollment_routes import enrollment_router

app = FastAPI()

app.include_router(enrollment_router)