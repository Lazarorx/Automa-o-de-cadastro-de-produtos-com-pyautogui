import flake8
import pyautogui  # Para automatizar o movimento do mouse e do teclado
from time import sleep  # Para pausar a execução por alguns segundos

# Passos manuais para realizar este processo de automação.

# 1 - clicar e digitar o usuário
pyautogui.click(981, 543, duration=1)
pyautogui.write('LAZAROXAVIER')
# 2 - clicar e digitar a senha
pyautogui.click(976, 563, duration=1)
pyautogui.write('L@zaro00')
# 3 - clicar e entrarLAZAROXAVIER
pyautogui.click(865, 597, duration=1)
# 4 - Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        # 1 - clicar e digitar produtoProduto 1Produto 1
        pyautogui.click(739, 525, duration=1)
        pyautogui.write(produto)
        # 2 - clicar e digitar quantidade
        pyautogui.click(719, 555, duration=1)
        pyautogui.write(quantidade)
        # 3 - clicar e digitar preço
        pyautogui.click(716, 579, duration=1)
        pyautogui.write(preco)
        # 4 - clicar em registrar
        pyautogui.click(582, 744, duration=1)
        sleep(1)
