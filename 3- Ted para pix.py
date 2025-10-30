import pyautogui as pg
import pyperclip as pc
from time import sleep
import os

CAMINHO_IMAGENS = '3- TED para PIX'
pg.PAUSE = 0.4
pg.alert("O código irá começar")

lancamentos_alterados = 500 # selecionar a quantidade de lançamentos que a automação irá alterar
caracteres_deletar = 30

# Função auxiliar para saber o caminho da imagem
def caminho_imagem(nome_imagem):
    return os.path.join(CAMINHO_IMAGENS, nome_imagem)

# Função para buscar uma lista de imagens até encontrar
def encontrar_imagens(imagens, confiança=0.7, grayscale=True):
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

# Função para retornar um valor aceito caso encontre ou não uma imagem na tela (para auxiliar no while)
def imagem_esta_na_tela(imagem, confiança=0.7, grayscale=True):
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
        imagem_encontrada, x, y, largura, altura = encontrar_imagens(
            ['Forma de Pagamento TED.png', 'Ativo Ted.png', 'Setas.png'], 0.7, grayscale=True
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
    encontrar_imagens(['Janela dados bancarios.png'])

    pg.click(985, 334)

    # Nota: O sistema TOTVS não permite seleção direta de texto neste campo nem o uso de comandos como 'ctrl+a' seguido de 'delete'.
    # Portanto, a abordagem adotada foi simular múltimos pressionamentos da tecla 'backspace',
    # garantindo a remoção completa do conteúdo atual antes da inserção do novo valor.
    for x in range(caracteres_deletar):
        pg.press('backspace')

    pc.copy("PIX - Dados Bancários") # Texto para padronização
    pg.hotkey('ctrl', 'v')

    imagem_encontrada, x, y, largura, altura = encontrar_imagens(['Lista forma de pagamento.png'], 0.7, grayscale=True)
    pg.click(x + largura / 2, y + altura / 2)

    imagem_encontrada, x, y, largura, altura = encontrar_imagens(['Pix Transf.png'], 0.7, grayscale=True)
    pg.click(x + largura / 2, y + altura / 2)
    sleep(0.4)
    
    pg.click(1091, 844)

    while imagem_esta_na_tela('Janela dados bancarios.png'):

        # Alguns cadastros apresentaram erro no CPF cadastrado. Essa parte é para evitar o código de quebrar (imagem foi removida da pasta)
        if imagem_esta_na_tela('CPF invalido.png', confiança=0.5):
            pg.press('enter')
            pg.click(1185,840)
            pg.press('enter')
        sleep(1)


    sleep(0.5)

    imagem_encontrada, x, y, largura, altura = encontrar_imagens(['Setas.png'])
    pg.click(x + largura / 1.5, y + altura / 1.3)