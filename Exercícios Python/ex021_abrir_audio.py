# Faça um programa que abra e reproduza o audio de um arquivo mp3

import pygame
import sys
import os

# Inicializa todos os módulos do pygame
pygame.init()
print("pygame inicializado.")

# Inicializa o mixer do pygame (responsável pelo áudio)
pygame.mixer.init()
print("Mixer inicializado.")

# Caminho do arquivo MP3
caminho_mp3 = "/Users/lucianaemanuelle/Library/CloudStorage/OneDrive-Pessoal/2. CURSOS PROGRAMAÇÃO/CURSO EM VIDEO - PYTHON/Aprendendo-Python/Exercícios Python/ex021_o_que_e_lgpd.mp3"

# Verifica o diretório de trabalho atual
print(f"Diretório de trabalho atual: {os.getcwd()}")

# Verifica se o arquivo MP3 existe
if not os.path.isfile(caminho_mp3):
    print(f"Arquivo {caminho_mp3} não encontrado.")
    sys.exit(1)
else:
    print(f"Arquivo {caminho_mp3} encontrado.")

try:
    # Carrega o arquivo MP3
    pygame.mixer.music.load(caminho_mp3)
    print(f"Arquivo {caminho_mp3} carregado com sucesso!")

    # Reproduz o arquivo MP3
    pygame.mixer.music.play()
    print("Reproduzindo...")

    # Mantém o programa em execução até que a música termine
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

except pygame.error as e:
    print(f"Erro ao carregar o arquivo MP3: {e}")
    sys.exit(1)

# Finaliza todos os módulos do pygame
pygame.quit()
print("pygame finalizado.")

# Mantém a janela aberta
input("Pressione Enter para sair...")
