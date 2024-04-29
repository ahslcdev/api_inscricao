from pydantic import BaseModel, Field


class ErrorMessageBadRequest(BaseModel):
    detail: str = Field(example='Algo inesperado aconteceu, entre em contato com o suporte.')