import pyautogui as pg
from time import sleep 
import pyperclip as pc
import pandas as pd
from pyautogui import ImageNotFoundException
import os

CAMINHO_IMAGENS = '8- Itau Unibanco'
pg.PAUSE = 0.3
pg.alert("O código irá começar")

nome_do_banco = 'Itaú Unibanco'

lancamentos_alterados = 500
caracteres_deletar = 23

def caminho_imagem(nome_imagem):
    return os.path.join(CAMINHO_IMAGENS, nome_imagem)

# Função para buscar uma imagem até encontrar
def encontrar_imagem(nome_imagem, confiança=0.7, grayscale=True):
    caminho_completo = os.path.join(CAMINHO_IMAGENS, nome_imagem)
    while True:
        try:
            # Tenta encontrar a imagem na tela
            resultado = pg.locateOnScreen(caminho_completo, grayscale=grayscale, confidence=confiança)
        
            # Se a imagem for encontrada, retorna as coordenadas
            if resultado:
                x, y, largura, altura = resultado
                return x, y, largura, altura
        except ImageNotFoundException:
            # Caso não encontre, espera 1 segundo e tenta novamente
            print(f"Imagem {nome_imagem} não encontrada. Tentando novamente...")
            sleep(1)

def imagem_esta_na_tela(imagem, confiança=0.7, grayscale=True):
    try:
        caminho = caminho_imagem(imagem)
        resultado = pg.locateOnScreen(caminho, confidence=confiança, grayscale=grayscale)
        return resultado is not None
    except:
        return False
    

def encontrar_terceira_seta(nome_imagem, caminho_imagens, confiança=0.7, grayscale=True):
    caminho_completo = os.path.join(caminho_imagens, nome_imagem)
    
    while True:
        try:
            resultado = pg.locateOnScreen(caminho_completo, grayscale=grayscale, confidence=confiança)

            if resultado:
                x, y, largura, altura = resultado
                
                # Dividir a largura em 4 partes (4 setas), e pegar a terceira
                largura_seta = largura // 4
                x_terceira = x + (2 * largura_seta) + (largura_seta // 2)
                y_centro = y + altura // 2

                return x_terceira, y_centro

        except Exception as e:
            print(f"Erro: {e}")
            print(f"Imagem {nome_imagem} não encontrada. Tentando novamente...")
            sleep(1)

for i in range(lancamentos_alterados):
    print(f'Comando de número: {i+1}')
    sleep(0.5)

    x, y, largura, altura = encontrar_imagem('1-cred 341.png', 0.7)
    pg.doubleClick(x + largura / 1.2, y + altura / 2)

    while imagem_esta_na_tela(['Janela dados bancarios.png']):
        sleep(1)

    sleep(0.5)
    pg.click(1171,574)

    pc.copy(nome_do_banco)
    
    # Nota: O sistema TOTVS não permite seleção direta de texto neste campo nem o uso de comandos como 'ctrl+a' seguido de 'delete'.
    # Portanto, a abordagem adotada foi simular múltimos pressionamentos da tecla 'backspace',
    # garantindo a remoção completa do conteúdo atual antes da inserção do novo valor.
    for x in range(caracteres_deletar):
        pg.press('backspace')

    pg.hotkey('ctrl','v')

    pg.click(1096,848)
    sleep(1)

    while imagem_esta_na_tela(['Janela dados bancarios.png']):
        sleep(1)


    nome_imagem = 'Setas.png'
    x, y = encontrar_terceira_seta(nome_imagem, CAMINHO_IMAGENS)
    pg.click(x, y)  # Clica no centro da terceira seta