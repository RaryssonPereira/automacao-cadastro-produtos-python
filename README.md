# Automacao de Cadastro de Produtos

**Autor:** Rarysson Pereira
**Formacao:** Analise e Desenvolvimento de Sistemas
**Ultima atualizacao:** 06/06/2025

---

## Objetivo do Projeto

Este projeto tem como objetivo automatizar o processo de cadastro de produtos em um sistema web, utilizando a biblioteca PyAutoGUI em Python. A automacao simula as acoes de um usuario real — como abrir o navegador, preencher formularios e pressionar teclas — com total precisao.

Essa automacao foi desenvolvida como parte dos estudos da trilha de Python Intensivao da Hashtag Treinamentos, voltada para iniciantes que desejam entender o uso prático de bibliotecas de automacao com foco em produtividade e simulacao de interacoes humanas com a interface grafica.

---

## Parte 1: Abertura do Navegador e Acesso ao Site

O script executa a seguinte sequencia:

* Abrir o menu de aplicativos do Ubuntu (atalho Super + A)
* Pesquisar pelo navegador Google Chrome
* Abrir o navegador
* Aguardar o carregamento da janela
* Digitar a URL do sistema de cadastro de produtos
* Pressionar Enter para acessar

Esse processo e feito de forma automatizada utilizando comandos da biblioteca `pyautogui`, com pausas controladas pelo modulo `time`.

---

## Bibliotecas Utilizadas

### 1. pyautogui

Utilizada para simular o controle do mouse, teclado, rolagem de tela e pressionamento de teclas. Permite interagir com qualquer elemento visual que esteja na tela do sistema operacional.

### 2. time

Biblioteca padrao do Python para criar pausas entre os comandos. Ideal para aguardar o carregamento de janelas ou campos.

---

## Instalacao no Ubuntu 24.04 LTS

### 1. Instalar o pip (se ainda nao estiver instalado)

```bash
sudo apt update
sudo apt install python3-pip -y
```

### 2. Instalar o PyAutoGUI com suas dependencias

```bash
pip3 install pyautogui --break-system-packages
```

### 3. Instalar dependencias adicionais para funcionamento correto:

```bash
sudo apt install scrot python3-tk python3-dev -y
```

Essas dependencias sao necessarias para o funcionamento do PyAutoGUI em ambientes Linux. O `scrot` permite capturas de tela, `tk` e `dev` sao utilizados por bibliotecas graficas e de entrada.

---

## Explicacao dos Comandos PyAutoGUI Usados

### `pyautogui.write("texto")`

Simula a digitacao de um texto como se fosse pelo teclado.

### `pyautogui.press("tecla")`

Pressiona uma tecla especifica (ex: "enter", "tab", "backspace").

### `pyautogui.click(x=..., y=...)`

Realiza um clique do mouse na coordenada especificada na tela.

### `pyautogui.scroll(valor)`

Rola a tela. Valor positivo sobe, valor negativo desce.

### `pyautogui.hotkey("tecla1", "tecla2")`

Simula o pressionamento combinado de teclas (ex: Ctrl + S ou Super + A).

### `pyautogui.PAUSE = tempo`

Define um tempo padrao de espera (em segundos) entre os comandos, evitando que os eventos acontecam rapido demais.

### `time.sleep(segundos)`

Cria pausas manuais para garantir que o sistema tenha tempo de responder, especialmente durante carregamentos de paginas.

---

## Consideracoes Finais

Este projeto e ideal para iniciantes que desejam aprender:

* Como funciona a interacao com o sistema operacional via Python
* Como automatizar tarefas repetitivas sem precisar de acesso ao codigo-fonte da aplicacao
* Como integrar arquivos de dados (como CSV) a formularios web de maneira automatizada

A automacao foi testada com sucesso no Ubuntu 24.04 LTS, utilizando Python 3.12 e Google Chrome.
