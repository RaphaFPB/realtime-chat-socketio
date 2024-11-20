# Chat em Tempo Real com Flask e Flask-SocketIO

Este projeto é uma implementação de um chat em tempo real utilizando Flask e Flask-SocketIO, onde a comunicação entre os clientes é realizada via WebSockets.

## Funcionalidades

- **Formulário de Nome de Usuário**: O usuário precisa inserir um nome de usuário antes de acessar o chat. Após preencher o nome, a seção de entrada de nome de usuário é escondida e a seção de chat é exibida.
- **Envio de Mensagens**: As mensagens são enviadas como objetos JSON, contendo o nome do usuário e o texto da mensagem.
- **Comunicação em Tempo Real**: Utilizando Flask-SocketIO, as mensagens são transmitidas em tempo real para todos os usuários conectados.

## Estrutura do Projeto

### index.html

O modelo de `index.html` foi baseado em um template fornecido pela plataforma **Rocketseat**. O template original contém as seguintes características:

- **Seção de Chat**:
  - Um formulário simples onde o usuário pode digitar mensagens.
  - As mensagens enviadas são mostradas em uma lista não ordenada (`<ul>`), sem distinção de usuário.

**Modificações Implementadas**:

- **Formulário de Nome de Usuário**:
  - Adicionei uma seção inicial onde o usuário deve inserir um nome de usuário antes de acessar o chat. Após o preenchimento do nome, a seção de nome de usuário é escondida e a seção de chat é exibida.
  
- **Envio de Mensagens com Dados Estruturados**:
  - Alterei o envio das mensagens para ser realizado como um objeto JSON. O objeto contém tanto o nome do usuário quanto o texto da mensagem (anteriormente, o template enviava apenas o texto da mensagem).
  - A estrutura de mensagem foi adaptada para incluir o nome do usuário ao exibir a mensagem no chat.

Essas modificações garantem uma experiência mais personalizada, com identificação do usuário e comunicação em formato estruturado.

### app.py

- **Flask**: Serve o template `index.html`.
- **Flask-SocketIO**: Permite a comunicação em tempo real entre os clientes.
  - Ao receber uma mensagem, o servidor emite a mensagem para todos os clientes conectados.
  - As mensagens são transmitidas como objetos JSON, contendo `user` (nome do usuário) e `text` (conteúdo da mensagem).

## Como Rodar o Projeto

### Requisitos

1. Python 3.x
2. Flask
3. Flask-SocketIO

### Instalação

1. Instale as dependências do projeto:

```bash
pip install flask flask-socketio
