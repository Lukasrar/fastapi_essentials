# fastapi

## Instalação

Crie e ative um ambiente virtual para instalar as dependências do projeto de
forma isolada:

```bash
python3 -m venv fastapienv
source fastapienv/bin/activate
```

- `python3 -m venv fastapienv` cria o ambiente virtual `fastapienv` no projeto.
- `source fastapienv/bin/activate` ativa esse ambiente no terminal atual. Os
  próximos pacotes instalados ficarão isolados do Python do sistema.

Com o ambiente ativado, instale o FastAPI e o servidor Uvicorn:

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

- `pip install fastapi` instala o framework FastAPI para criar a aplicação
  e suas rotas.
- `pip install "uvicorn[standard]"` instala o Uvicorn, servidor ASGI usado
  para executar a aplicação, junto com as dependências recomendadas para uso
  padrão. As aspas preservam `[standard]` como parte do nome do pacote no shell.
