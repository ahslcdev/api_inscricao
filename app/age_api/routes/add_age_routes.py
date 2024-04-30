from fastapi import Depends, HTTPException, status
from app.age_api.dependencies import ConfigAuth
from app.age_api.error_messages import ErrorMessageAgeGroupNotAuth, ErrorMessageBadRequest
from app.age_api.exceptions import AlreadyRegisteredAgeException, InvalidAgeException
from app.age_api.routes import router
from app.age_api.schemas import AgeGroup

from app.age_api.service import AgeGroupService
from app.age_api.utils import validate_ages

@router.post(
    "/",
    response_model=AgeGroup,
        responses={
        status.HTTP_400_BAD_REQUEST:{
            "model":ErrorMessageBadRequest
        },
        status.HTTP_401_UNAUTHORIZED:{
            "model":ErrorMessageAgeGroupNotAuth
        }
    }
)
async def add_age_group(age: AgeGroup, 
                        Verifcation = Depends(ConfigAuth.check_credentials)):
    """
    Este route é responsável por validar os dados da idade e por chamar
    o service que irá fazer o insert no banco de dados.
    """
    try:
        service = AgeGroupService()
        query = service.get_query()
        values = (query.min_age == age.min_age) & (query.max_age == age.max_age)
        ages = service.get_by_query(values)

        if ages:
            raise AlreadyRegisteredAgeException("Este grupo de idades já está cadastrado.")
        validate_ages(age.min_age, age.max_age)
        age_data = service.create_instance(age)
    except (AlreadyRegisteredAgeException, InvalidAgeException, Exception) as e:
       raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            str(e)
        )
    return age_data