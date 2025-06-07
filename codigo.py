# ---------------------------------------------------------------
# Autor: Rarysson Pereira
# Formação: Análise e Desenvolvimento de Sistemas
# Última atualização: 06/06/2025
# Descrição: Automação com PyAutoGUI para acessar site de login
# da aula de Python Intensivão da Hashtag Treinamentos.
# ---------------------------------------------------------------

import pyautogui  # Biblioteca para automação de mouse, teclado e tela
import time  # Biblioteca padrão para controle de tempo e pausas

# === Parte 1: Abertura do navegador e acesso ao link de cadastro ===

# Configura uma pausa de 0.7s entre cada comando do PyAutoGUI
pyautogui.PAUSE = 0.5 

# Abre o menu de aplicativos no Ubuntu usando Super + A
# (equivalente ao menu iniciar no Windows)
pyautogui.hotkey("win", "a")

# Digita "chrome" para localizar o navegador Google Chrome
pyautogui.write("chrome")

# Pressiona Enter para abrir o Chrome
pyautogui.press("enter")

# Aguarda o Chrome abrir
time.sleep(1.2)

# Digita a URL da página de login do cadastro
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# Aguarda para garantir que o campo da barra de endereços está ativo
time.sleep(1.2)

# Pressiona Enter para acessar o site
pyautogui.press("enter")

# Espera o carregamento da página
time.sleep(1.2)

# === Parte 2: Efetuar o login no sistema de cadastro ===

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
time.sleep(1.2)

# === Parte 3: Importar a base de dados .csv ===

import pandas  # Biblioteca para leitura e manipulação de dados em tabela (DataFrame)

# Lê o arquivo CSV com os produtos e armazena em formato de tabela
tabela = pandas.read_csv(
    "/home/rarysson/Documentos/aula1_python/automatizacao_de_cadastro/produtos.csv"
)

# === Parte 4: Cadastrar todos os produtos  ===

# Para cada linha da tabela produtos.csv, um produto será cadastrado no formulário
for linha in tabela.index:

    # Clica no campo de "Código do Produto"
    pyautogui.click(x=897, y=323)

    # Captura e escreve o código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Captura e escreve a marca do produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Captura e escreve o tipo do produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Captura e escreve a categoria (transformada em string)
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Captura e escreve o preço unitário do produto
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    # Captura e escreve o custo do produto
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # Captura a observação do produto (se existir) e escreve
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):  # Verifica se é diferente de NaN
        pyautogui.write(str(obs))
    else:
        pyautogui.write("")

    pyautogui.press("tab")

    # Pressiona Enter para enviar o formulário
    pyautogui.press("enter")

    # Sobe a tela para garantir que o formulário volte ao topo
    pyautogui.scroll(10000)
    # Alternativamente: pyautogui.press("home")

# === Fim da automação ===
