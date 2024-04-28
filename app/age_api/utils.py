import json


def load_credentials():
    with open("app/age_api/credentials.json", "r") as file:
        return json.load(file)