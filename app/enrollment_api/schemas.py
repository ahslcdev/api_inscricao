from pydantic import BaseModel

from app.age_api.service import AgeGroupService

class EnrollmentSchema(BaseModel):
    name: str
    cpf: str
    age: int

    