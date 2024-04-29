from typing import Dict
from fastapi import Depends, status, HTTPException
from app.age_api.configs import ConfigAuth
from app.age_api.error_messages import ErrorMessageAgeGroupNotAuth, ErrorMessageAgeGroupNotFound, ErrorMessageBadRequest
from app.age_api.exceptions import AgeGroupNotFound
from app.age_api.routes import router

from app.age_api.service import AgeGroupService

@router.delete(
    "/{id}/",
    responses={
        status.HTTP_400_BAD_REQUEST:{
            "model":ErrorMessageBadRequest
        },
        status.HTTP_401_UNAUTHORIZED:{
            "model":ErrorMessageAgeGroupNotAuth
        },
        status.HTTP_404_NOT_FOUND:{
            "model":ErrorMessageAgeGroupNotFound
        },
        status.HTTP_200_OK:{
            "content": {
                "application/json": {
                    "example": 
                        {
                            "message": "Grupo de idade deletado com sucesso.",
                        }
                }
            },
        }
    }
)
async def delete_age_group(id: int,
                           Verifcation = Depends(ConfigAuth.check_credentials)):
    """
    Endpoint responsável por deletar um objeto no banco de dados.

    :params id: ID do objeto que deseja deletar.
    """
    try:
        service = AgeGroupService()
        age_group = service.get_by_id(id)
        if not age_group:
            raise AgeGroupNotFound('Grupo de idade não encontrado.')
        service.delete_by_id(id)
    except AgeGroupNotFound as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            str(e)
        )
    except Exception as e:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            str(e)
        )
    return {"message":"Grupo de idade deletado com sucesso."}