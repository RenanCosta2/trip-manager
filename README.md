# Trip Manager

## 📋 Visão Geral

Este projeto foi desenvolvido como parte de um curso da **Rocketseat**. O objetivo é ajudar o usuário a organizar viagens à trabalho ou lazer. O usuário pode criar uma viagem com nome, data de início e fim. Dentro da viagem, o usuário pode planejar sua viagem adicionando atividades para realizar em cada dia.

## 🚀 Requisitos Funcionais

### 1. Cadastro de Viagem

Permite que o usuário cadastre uma viagem fornecendo as seguintes informações:
- **Local de destino**
- **Data de início**
- **Data de término**
- **E-mails dos convidados**
- **Nome completo**
- **Endereço de e-mail**

### 2. Confirmação de Viagem

- O criador da viagem recebe um e-mail com um link para confirmar a viagem.
- Ao clicar no link:
  - A viagem é confirmada.
  - Os convidados recebem e-mails de confirmação de presença.
  - O criador é redirecionado para a página da viagem.

### 3. Confirmação de Presença dos Convidados

- Os convidados, ao clicarem no link de confirmação, são redirecionados para a aplicação.
- Devem inserir seu nome (além do e-mail já preenchido) para confirmar a presença na viagem.

### 4. Adição de Links Importantes

- Na página do evento, os participantes podem adicionar links úteis, como:
  - Reservas de hospedagem (ex.: Airbnb)
  - Locais a serem visitados
  - Outros recursos relevantes

### 5. Adição de Atividades

- Permite que o criador e os convidados adicionem atividades que ocorrerão durante a viagem, incluindo:
  - **Título da atividade**
  - **Data**
  - **Horário**

### 6. Convite de Novos Participantes

- Possibilita convidar novos participantes diretamente da página do evento através do e-mail.
- Novos participantes seguem o mesmo fluxo de confirmação que os convidados iniciais.

## 🛠️ Tecnologias Utilizadas

- Linguagem Python
- Framework Flask
- Banco de dados SQLite

## 📦 Estrutura de Pastas

- `/routes`: pasta responsável por configurar as rotas
- `/server`: pasta para configurar o servidor
- `/repositories`: pasta responsável pelas ações no banco de dados
- `/settings`: pasta responsável pela conexão com banco de dados
- `/controllers`: pasta dos controllers do sistema

## 🚀 Como Configurar o Projeto

1. Configuração padrão do ambiente virtual venv.
     ```bash
      python3 -m venv venv # On Windows use `python -m venv venv`
      source venv/bin/activate  # On Windows use `env\Scripts\activate`
    ```
2. Deverá ser instalado o framework Flask.
     ```bash
      pip3 install Flask
    ```
3. As dependências para executar os testes e enviar o email.
     ```bash
      pip3 install requests 
      pip3 install pytest
    ```
