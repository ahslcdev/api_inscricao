from fastapi import Depends, HTTPException, status
from app.age_api.configs import ConfigAuth
from app.age_api.error_messages import ErrorMessageAgeGroupNotAuth, ErrorMessageAgeGroupNotFound, ErrorMessageBadRequest
from app.age_api.exceptions import AgeGroupNotFound
from app.age_api.routes import router

from app.age_api.schemas import AgeGroup
from app.age_api.service import AgeGroupService

@router.get(
    "/{id}/",
    response_model=AgeGroup,
    responses={
        status.HTTP_400_BAD_REQUEST:{
            "model":ErrorMessageBadRequest
        },
        status.HTTP_401_UNAUTHORIZED:{
            "model":ErrorMessageAgeGroupNotAuth
        },
        status.HTTP_404_NOT_FOUND:{
            "model":ErrorMessageAgeGroupNotFound
        }
    }
)
async def retrieve_age_group(id: int,
                             Verifcation = Depends(ConfigAuth.check_credentials)):
    """
    Este route é responsável por buscar no banco de dados o grupo de idade
    de ID informado.

    :params id: ID do objeto que se deseja buscar no banco de dados
    """
    try:
        service = AgeGroupService()
        age_group = service.get_by_id(id)
        if not age_group:
            raise AgeGroupNotFound('Grupo de idade não encontrado.')
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
    return age_group