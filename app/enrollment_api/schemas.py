from pydantic import BaseModel, validator

from app.age_api.service import AgeGroupService
from app.enrollment_api.exceptions import InvalidCPF
from app.enrollment_api.utils import validate_cpf

class EnrollmentSchema(BaseModel):
    name: str
    age: str = None
    cpf: str
    age: int

    @validator('cpf')
    def valid_cpf(cls, value):
        if not validate_cpf(value):
            raise InvalidCPF("CPF must have 11 digits")
        return value
    
    @validator('age')
    def valid_age(cls, value):
        instange_service =  AgeGroupService()
        query = instange_service.get_query()
        values = (query.min_age <= value) & (query.max_age >= value)
        ages = instange_service.get_by_query(values)
        if not ages:
            raise InvalidCPF("Invalido")
        return value