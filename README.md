# 🚀 Automacao de Cadastro de Produtos

👤 **Autor:** Rarysson Pereira
🎓 **Formacao:** Analise e Desenvolvimento de Sistemas
📅 **Ultima atualizacao:** 06/06/2025

---

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo automatizar o processo de cadastro de produtos em um sistema web, utilizando a biblioteca **PyAutoGUI** com **Python**. A automacao simula as acoes de um usuario real: abrir o navegador, preencher formularios e pressionar teclas — tudo de forma precisa e automatica.

Este projeto foi desenvolvido como parte dos estudos da trilha de Python Intensivao da Hashtag Treinamentos, ideal para iniciantes que desejam aprender automacao de tarefas visuais.

---

## 🧰 Bibliotecas Utilizadas

### 📦 pyautogui

Biblioteca para controle automatizado do mouse, teclado e tela.

### ⌛ time

Biblioteca padrao do Python utilizada para criar pausas entre comandos.

---

## 🐧 Instalacao no Ubuntu 24.04 LTS

### 🔧 1. Instalar o pip (caso ainda nao tenha)

```bash
sudo apt update
sudo apt install python3-pip -y
```

### 📥 2. Instalar o PyAutoGUI

```bash
pip3 install pyautogui --break-system-packages
```

### 📦 3. Instalar dependencias adicionais

```bash
sudo apt install scrot python3-tk python3-dev -y
```

> Essas dependencias garantem o funcionamento completo do PyAutoGUI em ambientes graficos Linux.

---

## 🧠 Comandos Basicos do PyAutoGUI

| Comando                         | Funcao                                            |
| ------------------------------- | ------------------------------------------------- |
| `pyautogui.write("texto")`      | ✍️ Digita texto como no teclado                   |
| `pyautogui.press("tecla")`      | ⌨️ Pressiona uma tecla unica (ex: "enter", "tab") |
| `pyautogui.click(x=..., y=...)` | 🖱️ Clica na posicao da tela informada            |
| `pyautogui.scroll(valor)`       | 🔃 Rola a tela para cima ou para baixo            |
| `pyautogui.hotkey("ctrl", "s")` | 🎹 Pressiona combinacoes de teclas                |
| `pyautogui.PAUSE = tempo`       | ⏸️ Adiciona pausa padrao entre os comandos        |
| `time.sleep(segundos)`          | 💤 Pausa manual para aguardar carregamentos       |

---

## 🌐 Parte 1: Abertura do Navegador e Acesso ao Site

A primeira parte do script executa as seguintes etapas:

* 🧭 Abre o menu de aplicativos do Ubuntu (atalho Super + A)
* 🔎 Pesquisa pelo navegador Google Chrome
* 🌍 Abre o navegador
* ⏱️ Aguarda o carregamento da janela
* 🔗 Digita a URL do sistema de cadastro
* ⌨️ Pressiona Enter para acessar

Essas acoes sao realizadas com comandos do `pyautogui`, com pausas entre etapas usando o modulo `time`.

---

## 🔐 Parte 2: Efetuar o Login no Sistema de Cadastro

Esta etapa da automacao tem como objetivo simular o preenchimento do formulario de login do sistema. Ela e responsavel por:

* Posicionar o cursor no campo de e-mail
* Digitar o endereco de e-mail do usuario
* Passar para o campo de senha
* Digitar a senha
* Submeter o formulario pressionando Enter

Essas acoes garantem o acesso ao ambiente do sistema onde os produtos serao posteriormente cadastrados.

**Etapas realizadas:**

* 🖱️ Clique na coordenada do campo de e-mail (posicao exata da tela)
* ⌨️ Digitacao do e-mail de acesso
* ➡️ Avanco para o campo seguinte com tecla `tab`
* 🔒 Digitacao da senha
* ⌨️ Enter para submeter o formulario
* ⏱️ Pausa com `time.sleep` para aguardar o carregamento da nova tela

---
