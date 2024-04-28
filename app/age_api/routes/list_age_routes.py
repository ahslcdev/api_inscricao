from fastapi import Depends
from app.age_api.configs import ConfigAuth
from app.age_api.routes import router

from app.age_api.service import AgeGroupService

@router.get("/")
async def list_age_groups(Verifcation = Depends(ConfigAuth.check_credentials)):
    ages = AgeGroupService().get_instances()
    return ages