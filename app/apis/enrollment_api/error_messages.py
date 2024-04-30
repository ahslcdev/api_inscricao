from pydantic import BaseModel, Field


class ErrorMessageBadRequest(BaseModel):
    detail: str = Field(json_schema_extra={"detail":'Algo inesperado aconteceu, entre em contato com o suporte.'})