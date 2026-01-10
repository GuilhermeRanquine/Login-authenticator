# 🏦 Authenticator Bank

O Authenticator Bank é um sistema de autenticação via terminal desenvolvido em Python. O projeto permite a criação de contas de utilizador e a validação de login através do armazenamento de dados num ficheiro persistente .csv.

Este projeto foi construído para demonstrar conceitos fundamentais de programação, como modularização, manipulação de ficheiros (I/O) e fluxo de controle.

## 🚀 Funcionalidades

- Registo de Utilizadores: Captura de dados (Nome, CPF, Email, etc.) e gravação segura em CSV.

- Sistema de Login: Validação de credenciais comparando inputs com a base de dados local.

- Fluxo de Navegação Inteligente: Menos menus redundantes e navegação fluida após o cadastro.

- Armazenamento Persistente: Os dados não se perdem ao fechar o programa.

## 🛠️ Tecnologias Utilizadas

Linguagem: Python 3.x

Armazenamento: CSV (Comma-Separated Values)

Módulos Nativos: csv, os, sys

## 📋 Como Executar

Certifica-te de que tens o Python instalado.

Clona este repositório ou faz o download dos ficheiros.

No terminal, navega até à pasta do projeto e executa:

```
python main.py
```

## 🔍 Exemplo de Uso

Ao iniciar o programa, terás o seguinte menu:

Create Account: Introduz os teus dados. Após o registo, podes escolher ir diretamente para o login ou sair.

Login: Valida o teu email e senha para aceder ao sistema.

## 🛠️ Melhorias Futuras (Roadmap)

Como este é um projeto educativo para portefólio, as próximas etapas planeadas são:

[ ] Segurança: Implementar Hashing de senhas (não guardar texto limpo).

[ ] Validação: Adicionar verificações de formato de email e CPF.

[ ] Interface: Evoluir do terminal para uma GUI (Interface Gráfica) ou Web
