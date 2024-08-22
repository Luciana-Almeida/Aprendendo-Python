# Desafio 62: Melhore o Desafio 061 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

# Solicita o primeiro termo e a razão da PA
primeiro_termo = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))

contador = 1
termo_atual = primeiro_termo
total_termos = 10
mais_termos = total_termos

while mais_termos != 0:

    while contador <= total_termos:
        print(f"{contador}º termo: {termo_atual}")
        termo_atual += razao
        contador += 1

    mais_termos = int(input("Quantos termos a mais você quer mostrar? (Digite 0 para encerrar) "))
    total_termos += mais_termos

print(f"Programa encerrado. Foram mostrados {total_termos} termos.")
