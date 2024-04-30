from typing import List
from fastapi import Depends, HTTPException, status
from app.apis.age_api.dependencies import ConfigAuth
from app.apis.age_api.error_messages import ErrorMessageAgeGroupNotAuth, ErrorMessageBadRequest
from app.apis.age_api.routes import router

from app.apis.age_api.schemas import AgeGroup
from app.apis.age_api.service import AgeGroupService

@router.get(
    "/",
    response_model=List[AgeGroup],
    responses={
        status.HTTP_400_BAD_REQUEST:{
            "model":ErrorMessageBadRequest
        },
        status.HTTP_401_UNAUTHORIZED:{
            "model":ErrorMessageAgeGroupNotAuth
        }
    }
)
async def list_age_groups(Verifcation = Depends(ConfigAuth.check_credentials)):
    """
    Este route é responsável por realizar a listagem dos grupos de idade
    cadastrados no banco de dados.
    """
    try:
        ages = AgeGroupService().get_instances()
    except Exception as e:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            ErrorMessageBadRequest(detail='Algo inesperado aconteceu, entre em contato com o suporte.').detail
        )
    return ages