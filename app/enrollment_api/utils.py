def validate_cpf(cpf):
    # Remove alguns caracteres indesejados
    cpf = ''.join([c for c in cpf if c.isdigit()])

    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (sequências invalidas)
    if cpf == cpf[0] * len(cpf):
        return False

    # Validação do primeiro dígito
    for i in range(9, 11):
        value = sum((int(cpf[num]) * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != int(cpf[i]):
            return False

    return True