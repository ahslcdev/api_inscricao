from typing import List
from fastapi import Depends, HTTPException, status
from app.age_api.configs import ConfigAuth
from app.age_api.error_messages import ErrorMessageAgeGroupNotAuth, ErrorMessageBadRequest
from app.age_api.routes import router

from app.age_api.schemas import AgeGroup
from app.age_api.service import AgeGroupService

@router.get("/",
            response_model=List[AgeGroup],
            responses={
                status.HTTP_400_BAD_REQUEST:{
                    "model":ErrorMessageBadRequest
                },
                status.HTTP_401_UNAUTHORIZED:{
                    "model":ErrorMessageAgeGroupNotAuth
                }
            })
async def list_age_groups(Verifcation = Depends(ConfigAuth.check_credentials)):
    try:
        ages = AgeGroupService().get_instances()
    except Exception as e:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            ErrorMessageBadRequest(detail='Alto inesperado aconteceu, entre em contato com o suporte.').detail
        )
    return ages