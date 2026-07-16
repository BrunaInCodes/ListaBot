# ListaBot

Robô de atendimento (ChatterBot) para o tema **Gerenciamento de Dados em Planilhas / Lista de Compras**, com acesso via sala de bate-papo web (Socket.IO).

## Estrutura

- `robo.py` — inicializa o ChatterBot e fornece as respostas.
- `treinamento.py` — treina o robô com os arquivos JSON em `conversas/`.
- `servico.py` — serviço Flask que expõe o robô via API (porta 6000).
- `testes.py` — casos de teste automatizados (unittest).
- `conversas/` — dicionários JSON com saudações e perguntas/respostas do tema.
- `chat/` — aplicação Node.js (Express + Socket.IO) com a interface de chat web.

## Como executar

1. Instale as dependências Python: `pip install -r requirements.txt`
2. Treine o robô: `python treinamento.py`
3. Inicie o serviço: `python servico.py`
4. Em outro terminal, dentro de `chat/`: `npm install` e `npm start`
5. Acesse `http://localhost:3000` no navegador.

## Testes

Execute: `python testes.py`
