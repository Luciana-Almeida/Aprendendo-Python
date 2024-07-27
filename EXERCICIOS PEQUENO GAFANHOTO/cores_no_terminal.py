# Texto colorido no terminal usando sequências de escape ANSI

print("\033[31m" + "Este texto é vermelho" + "\033[0m")
print("\033[35m" + "Este texto é magenta" + "\033[0m")
print("\033[33m" + "Este texto é amarelo" + "\033[0m")
print("\033[32m" + "Este texto é verde" + "\033[0m")
print("\033[34m" + "Este texto é azul" + "\033[0m")
print("\033[36m" + "Este texto é ciano" + "\033[0m")
print("\033[37m" + "Este texto é cinza" + "\033[0m")

print("\033[1m" + "Este texto é negrito" + "\033[0m")
print("\033[4m" + "Este texto é sublinhado" + "\033[0m")

print("\033[0;30;41m" + "Este fundo é vermelho" + "\033[m")
print("\033[4;33;44m" + "Este fundo é azul" + "\033[m")
print("\033[1;35;43m" + "Este fundo é amarelo" + "\033[m")
print("\033[30;42m" + "Este fundo é verde" + "\033[m")
