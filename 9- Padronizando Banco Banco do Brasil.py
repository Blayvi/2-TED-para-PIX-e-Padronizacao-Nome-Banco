import pyautogui as pg
import pyperclip as pc
from time import sleep
import os

CAMINHO_IMAGENS = '9- Caminho Bancos'
pg.PAUSE = 0.3
pg.alert("O código irá começar")

lancamentos_alterados = 500
caracteres_deletar = 25
nome_banco = 'Banco do Brasil' # Esse código pode ser utilizado para qualquer outro banco (menos com o Itaú), basta trocar o nome_banco para o Banco desejado.

def caminho_imagem(nome_imagem):
    return os.path.join(CAMINHO_IMAGENS, nome_imagem)

# Função para buscar uma imagem até encontrar
def encontrar_imagem2(imagens, confiança=0.73, grayscale=True):
    if isinstance(imagens, str):
        imagens = [imagens]  # Garante que sempre seja uma lista

    imagens_caminho = [caminho_imagem(img) for img in imagens]

    while True:
        for imagem, img_path in zip (imagens, imagens_caminho):
            try:
                resultado = pg.locateOnScreen(img_path, grayscale=grayscale, confidence=confiança)
                if resultado:
                    x, y, largura, altura = resultado
                    #print(f"Imagem encontrada: {imagem}")
                    return imagem, x, y, largura, altura
            except Exception as e:
                print(f"Erro ao procurar imagem {imagem}: {e}")
        
        print(f"Nenhuma imagem encontrada. Tentando novamente...")
        sleep(0.4)

def imagem_esta_na_tela(imagem, confiança=0.65, grayscale=True):
    try:
        caminho = caminho_imagem(imagem)
        resultado = pg.locateOnScreen(caminho, confidence=confiança, grayscale=grayscale)
        return resultado is not None
    except:
        return False

for i in range(lancamentos_alterados):
    print(f'Comando de número: {i+1}')
    sleep(0.5)
    while True:
        imagem_encontrada, x, y, largura, altura = encontrar_imagem2(
            ['ativo pix transferencia.png','ativo pix.png','Ativo Ted.png', 'Setas.png'], 0.73, grayscale=True
        )

        if imagem_encontrada == 'Setas.png':
            #print("Setas encontradas. Descendo a tela...")
            pg.click(x + largura / 1.5, y + altura / 1.3)
            sleep(0.5)
            # Depois da ação, volta a procurar somente as duas primeiras
            continue  # volta ao início do while e tenta novamente
        else:
            break  # saiu do while pois encontrou uma das imagens desejadas

    # Se chegou aqui, encontrou uma imagem válida (TED ou Ativo TED)
    pg.doubleClick(x + largura / 2, y + altura / 1.4)
    sleep(0.6)
    encontrar_imagem2(['Janela dados bancarios.png'])

    pg.click(1182, 573)

    # Nota: O sistema TOTVS não permite seleção direta de texto neste campo nem o uso de comandos como 'ctrl+a' seguido de 'delete'.
    # Portanto, a abordagem adotada foi simular múltimos pressionamentos da tecla 'backspace',
    # garantindo a remoção completa do conteúdo atual antes da inserção do novo valor.
    for x in range(caracteres_deletar):
        pg.press('backspace')

    pc.copy(nome_banco)
    pg.hotkey('ctrl', 'v')
    pg.click(1091, 844)

    while imagem_esta_na_tela(['Janela dados bancarios.png']):
        sleep(0.7)

    _, x, y, largura, altura = encontrar_imagem2(['Setas.png'])
    pg.click(x + largura / 1.5, y + altura / 1.3)
    sleep(0.5)