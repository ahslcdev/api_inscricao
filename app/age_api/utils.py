import json

from app.age_api.exceptions import InvalidAgeException


def load_credentials():
    with open("app/age_api/credentials.json", "r") as file:
        return json.load(file)
    

def validate_ages(min_age: int, max_age: int):
    if min_age > max_age or min_age <= 0 or max_age <= 0:
        raise InvalidAgeException("Dados de idade mínima e máxima são inválidos.")