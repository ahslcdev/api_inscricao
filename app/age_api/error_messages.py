
from pydantic import BaseModel, Field


class ErrorMessageAgeGroupNotAuth(BaseModel):
    detail: str = Field(example='Dados de acesso incorretos.')


class ErrorMessageBadRequest(BaseModel):
    detail: str = Field(example='Algo inesperado aconteceu, entre em contato com o suporte.')


class ErrorMessageAgeGroupNotFound(BaseModel):
    detail: str = Field(example='Não encontrado.')