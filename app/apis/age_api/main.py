from fastapi import FastAPI
from app.apis.age_api.routes.age_routes import age_router

app = FastAPI(
    title='API',
    version='0.1.0'
)

app.include_router(age_router)
