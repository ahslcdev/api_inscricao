
from pydantic import BaseModel, Field


class ErrorMessageAgeGroupNotAuth(BaseModel):
    detail: str = Field(json_schema_extra={"detail":'Dados de acesso incorretos.'})


class ErrorMessageBadRequest(BaseModel):
    detail: str = Field(json_schema_extra={"detail":'Algo inesperado aconteceu, entre em contato com o suporte.'})


class ErrorMessageAgeGroupNotFound(BaseModel):
    detail: str = Field(json_schema_extra={"detail":'Não encontrado.'})