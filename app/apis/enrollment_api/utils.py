from app.apis.age_api.service import AgeGroupService
from app.apis.enrollment_api.exceptions import InvalidAge


def validate_cpf(cpf):
    """
    Função para validar CPF
    """
    cpf = ''.join([c for c in cpf if c.isdigit()])

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * len(cpf):
        return False

    for i in range(9, 11):
        value = sum((int(cpf[num]) * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != int(cpf[i]):
            return False

    return True


def validate_age(value):
    """
    Função para validar idades
    """
    if value <= 0:
        raise InvalidAge("Idade não pode ser menor que 0")
    instange_service =  AgeGroupService()
    query = instange_service.get_query()
    values = (query.min_age <= value) & (query.max_age >= value)
    ages = instange_service.get_by_query(values)
    if not ages:
        raise InvalidAge("Esta idade não está disponível.")
    
    return value