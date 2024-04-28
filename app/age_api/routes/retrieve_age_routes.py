from fastapi import Depends
from app.age_api.configs import ConfigAuth
from app.age_api.routes import router

from app.age_api.service import AgeGroupService

@router.get("/{id}/")
async def retrieve_age_group(id: int,
                             Verifcation = Depends(ConfigAuth.check_credentials)):
    service = AgeGroupService()
    return service.get_by_id(id)