# Creative Drive

## Começando <a name = "getting_started"></a>

### Antes de tudo rode esses comandos

- Criar o novo ambiente:

```
    virtualenv ENV
```

- Acessar o diretório do ambiente:

```
cd ENV
```

- Copiar o projeto para o diretório do ambiente, incluindo o arquivo requirements.txt;

- Ativar o ambiente:

```
bin/activate
```

- Instalar as dependências do projeto:

```
pip install -r requirements.txt
```

- Comando para criar o Banco de Dados SQLite

```
python manage.py migrate
```

- comando para criar um superuser

```
python manage.py createsuperuser
```

- Configurar da seguinte forma: <br>
  username: Willian <br>
  password: 1234

### Após esses passos, para rodar a API:

- Execute o comando:

```
python manage.py runserver
```

# Desafios não alcançados

Infelizmente não consegui completar o desafio inteiro, na API faltou:

- Fazer upload de arquivos, fiz somente de 1 imagem por vez. Dá para acessar pela rota: http://127.0.0.1:8000/arquives/
- Feedback para o usuario sobre o status da transferência do arquivo.
- Listagem e download dos aquivos listados na pasta uploads
