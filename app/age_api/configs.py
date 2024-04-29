from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException, status

from app.age_api.utils import load_credentials

class ConfigAuth:

    @staticmethod
    def check_credentials(creds: HTTPBasicCredentials = Depends(HTTPBasic()), 
                          auth_data=Depends(load_credentials)):
        username = creds.username
        password = creds.password
        if username in auth_data.get('users') and password == auth_data.get('users')[username]["password"]:
            return True
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Dados de acesso incorretos.",
                headers={"WWW-Authenticate": "Basic"},
            )
   