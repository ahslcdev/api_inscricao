from fastapi import Depends
from app.age_api.configs import ConfigAuth
from app.age_api.routes import router
from app.age_api.schemas import AgeGroup
from pydantic import BaseModel, Field
from tinydb import TinyDB, Query

from app.age_api.service import AgeGroupService

class ErrorMessageAgeGroupNotFound(BaseModel):
    detail: str = Field(example='Grupo de idade não encontrado.')


db = TinyDB('app/db.json')

@router.delete(
        "/{id}/",
        # response_model=AgeGroup,
        # status_code=200,
        # responses={
        #     404:{
        #         "model": ErrorMessageAgeGroupNotFound,
        #     },
        # }
)
async def delete_age_group(id: int,
                           Verifcation = Depends(ConfigAuth.check_credentials)):
    """
    Endpoint responsável por deletar um objeto no banco de dados.

    :params id: ID do objeto que deseja deletar.
    """
    AgeGroupService().delete_by_id(id)
    return {"message": "Endpoint from API 2"}