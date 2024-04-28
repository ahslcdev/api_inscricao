import time
from fastapi import Depends
from app.age_api.configs import ConfigAuth
from app.age_api.routes import router
from app.age_api.schemas import AgeGroup

from app.age_api.service import AgeGroupService

@router.post("/")
async def add_age_group(age: AgeGroup, 
                        Verifcation = Depends(ConfigAuth.check_credentials)):
    try:
        age_id = AgeGroupService().create_instance(age)
        return age_id
    except Exception as e:
        print(f"{e}")
        return f"{e}"