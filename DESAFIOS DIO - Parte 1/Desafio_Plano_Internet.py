# Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados. 

# Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

def recomendar_plano(consumo):
    if consumo <= 10:
        return "A recomendação ideal para você é o Plano Essencial Fibra - 50Mbps!"
    
    elif 10 < consumo <= 20:
        return "A recomendação ideal para você é o Plano Prata Fibra - 100Mbps!"
    
    else:
        return "A recomendação ideal para você é o Plano Premium Fibra - 300Mbps!"
    
consumo = float(input("Informe o valor da sua média de consumo mensal (em GB): "))
print(recomendar_plano(consumo))