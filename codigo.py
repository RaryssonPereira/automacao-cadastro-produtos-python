# ---------------------------------------------------------------
# Autor: Rarysson Pereira
# Formação: Análise e Desenvolvimento de Sistemas
# Última atualização: 06/06/2025
# Descrição: Automação com PyAutoGUI para acessar site de login
# da aula de Python Intensivão da Hashtag Treinamentos.
# ---------------------------------------------------------------

import pyautogui
import time

# Parte 1: Abertura do navegador e acesso ao link de cadastro.

# Configura uma pausa de 0.7s entre cada comando do PyAutoGUI
pyautogui.PAUSE = 0.6

# Abre o menu de aplicativos no Ubuntu usando Super + A
# (equivalente ao menu iniciar no Windows)
pyautogui.hotkey("win", "a")  # "super" também pode funcionar

# Digita "chrome" para localizar o navegador Google Chrome
pyautogui.write("chrome")

# Pressiona Enter para abrir o Chrome
pyautogui.press("enter")

# Aguarda o Chrome abrir
time.sleep(1.0)

# Digita a URL da página de login do cadastro
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# Aguarda para garantir que o campo da barra de endereços está ativo
time.sleep(1.0)

# Pressiona Enter para acessar o site
pyautogui.press("enter")

# Espera o carregamento da página
time.sleep(1.6)


# Parte 2: Efetuar o login

# Clica no campo e-mail
pyautogui.click(x=882, y=438)

# Escreve sua conta de e-mail (exemplo)
pyautogui.write("tatto@exemplo.com.br") 

# Para ir para próximo campo
pyautogui.press("tab")

# Escreve sua senha
pyautogui.write("senhaforte")

# Para ir para próximo campo
pyautogui.press("tab")

# Dá enter para logar na sua conta do sistema de cadastro (apenas um site que simula um sistema de cadastro)
pyautogui.press("enter")

# Espera o carregamento da página
time.sleep(2)

# Parte 3: Importar a base de dados .csv
# Esta etapa usa a biblioteca pandas para ler o arquivo com os
# dados dos produtos que serão cadastrados automaticamente.

# Importa a biblioteca pandas, utilizada para leitura e manipulação de dados em tabelas
import pandas

# Lê o arquivo 'produtos.csv' e armazena o conteúdo em forma de tabela (DataFrame)
# Cada linha representa um produto, e cada coluna representa uma informação (nome, preço, descrição, etc.)
tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Parte 4: Cadastrar um produto

time.sleep(2)
#pyautogui.press("tab")
pyautogui.click(x=133, y=48)
pyautogui.click(x=897, y=323)
codigo = "MOLO000251"
pyautogui.write(codigo) #Código do produto
pyautogui.press("tab")

marca = "Logitech"
pyautogui.write(marca) #Marca do Produto
pyautogui.press("tab")

tipo = "Mouse"
pyautogui.write(tipo) #Tipo de Produto
pyautogui.press("tab")

categoria = "1"
pyautogui.write(categoria) #Categoria do produto
pyautogui.press("tab")

preco_unitario = "25.95"
pyautogui.write(preco_unitario) #Preço unitário do produto
pyautogui.press("tab")

custo = "6.50"
pyautogui.write(custo) #Custo do produto
pyautogui.press("tab")

obs = ""
pyautogui.write(obs) #Observação/detalhes do produto
pyautogui.press("tab")

#pyautogui.press("enter") #Botao para Cadastrar o produto

# Parte 5: Repetir o cadastro para todos os outros produtos

