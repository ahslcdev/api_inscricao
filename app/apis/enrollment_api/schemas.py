from pydantic import BaseModel

class EnrollmentSchema(BaseModel):
    name: str
    cpf: str
    age: int

    