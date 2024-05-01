import json

from app.apis.age_api.exceptions import InvalidAgeException


def load_credentials():
    """
    Utilizado para carregar o arquivo de credenciais
    """
    with open("app/apis/age_api/credentials.json", "r") as file:
        return json.load(file)
    

def validate_ages(min_age: int, max_age: int):
    """
    Função que valida as idades mínima e máxima informadas.
    """
    if min_age > max_age or min_age <= 0 or max_age <= 0:
        raise InvalidAgeException("Dados de idade mínima e máxima são inválidos.")