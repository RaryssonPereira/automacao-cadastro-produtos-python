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

## 🌐 Parte 1: Abertura do Navegador e Acesso ao Site de Cadastro

Esta etapa inicial automatiza a abertura do Google Chrome no Ubuntu e o acesso ao link da página de login do sistema de cadastro da Hashtag Treinamentos.

A sequência de comandos simula as ações de um usuário real:

- 🧭 Abre o menu de aplicativos do Ubuntu (`Super + A`);
- 🔎 Digita “chrome” para localizar o navegador;
- 🌍 Abre o navegador Google Chrome;
- ⏱️ Aguarda o carregamento da janela;
- 🔗 Digita a URL do sistema de cadastro;
- ⌨️ Pressiona Enter para acessar o site.

Essa etapa garante que a automação inicie exatamente na tela de login do sistema, pronta para realizar os próximos passos.

---

## 🔐 Parte 2: Efetuar o Login no Sistema de Cadastro

Após acessar a página de login, esta etapa automatiza o preenchimento dos campos de e-mail e senha, simulando o login de um usuário no sistema.

As ações realizadas são:

- 📧 Clica no campo de e-mail;
- ✍️ Digita o endereço de e-mail (exemplo usado: `tatto@exemplo.com.br`);
- 🔀 Usa a tecla Tab para navegar até o campo de senha;
- 🔒 Digita a senha (exemplo usado: `senhaforte`);
- ⏭️ Pressiona Tab novamente para avançar;
- ⏎ Pressiona Enter para realizar o login;
- ⏳ Aguarda o carregamento da próxima página após o login.

Essa etapa completa o acesso ao sistema, preparando o ambiente para o cadastro automático dos produtos.

---

## 📥 Parte 3: Importar a Base de Dados `.csv`

Nesta etapa, a automação carrega a base de dados com os produtos que serão cadastrados automaticamente no sistema.

As ações executadas são:

- 📚 Importa a biblioteca `pandas`, utilizada para manipulação de dados em formato de tabela (DataFrame);
- 📂 Lê o arquivo `produtos.csv` localizado no caminho indicado e armazena seu conteúdo em uma tabela na memória.

Essa tabela será utilizada nas próximas etapas para preencher automaticamente os campos do sistema com os dados de cada produto.

> 📝 Certifique-se de que o arquivo `produtos.csv` exista no caminho correto e esteja formatado com colunas válidas, como `nome`, `preco`, `quantidade`, etc.

---

## 📝 Parte 4: Cadastrar Todos os Produtos

Nesta etapa, o código percorre cada linha da tabela importada do `produtos.csv` e realiza o preenchimento automático do formulário de cadastro no site, campo por campo.

Para cada produto da tabela, as seguintes ações são realizadas:

- 🔢 Clica no campo "Código do Produto" e digita o código;
- 🏷️ Digita a marca, tipo e categoria do produto;
- 💲 Digita o preço unitário e o custo do produto;
- 🗒️ Preenche a observação (caso exista);
- ⏎ Pressiona Enter para enviar o formulário de cadastro;
- 🔝 Rola a página para o topo, preparando para o próximo cadastro.

Esse processo se repete automaticamente para cada linha da base de dados, garantindo o cadastro em lote de todos os produtos listados no arquivo `.csv`.

> ✅ Observação: O script verifica se o campo de observações está vazio (`NaN`) antes de preencher, garantindo que não sejam inseridos valores incorretos.

---
