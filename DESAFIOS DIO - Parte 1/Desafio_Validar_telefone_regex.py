# Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto.

import re

# Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
    # Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"
    
    # A função 're.match()' para verificar se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):
        # Retorne que o número de telefone é válido:
        return "Número de telefone válido."
    else:
        # Retorne que o número de telefone é inválido:
        return "Número de telefone inválido."

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input("Informe o número de telefone: ")

# Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)

