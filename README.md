## employee-register-service
Aplicação de serviço API Rest de cadastro de funcionários desenvolvida em Django.

## Route

`http://18.231.35.212/api/employee/create/`
- Requisição: POST

Route para o cadastro de funcionários, tem como campos obigatórios email, senha, nome e código postal brasileiro. Retorna um JSON com o email, nome, código postal e os campos endereço, bairro, cidade e estado - estes quatro últimos disponibilizados via consulta ao microsserviço.

Exemplo de requisição
- Entrada (form-data no body)
    - email: joaosantos@gmail.com
    - password: senha123
    - name: João Santos
    - postal_code: 09781250

- Saída (content-type application/json)
```
{
    "email": "joaosantos@gmail.com",
    "name": "João Santos",
    "postal_code": "09781250",
    "address": "Rua Papa Paulo VI (Jd Yrajá)",
    "neighborhood": "Santa Terezinha",
    "city": "São Bernardo do Campo",
    "state": "SP"
}
```

## Iniciando app local

O app é dockerizado, portanto é preciso montar a imagem e rodar o comando docker-compose.

Antes, é preciso configurar as variáveis de ambiente, criando um arquivo `variables.env` e inseri-las.
```
DB_HOST=db
DB_NAME=app
DB_USER=postgres
DB_PASS=supersecretpassword
SECRET_KEY=SECRETHASH
ADDRESS_SERVICE_AUTH_TOKEN=JWTOKEN-PAST-HERE
```

Depois montamos a imagem e iniciamos o app, na raiz do projeto:
```
docker build .
docker-compose up --build
```
O acesso estará disponível na porta 8000 do localhost

A aplicação é coberta de testes e  usado o lint flake8 para python, para rodá-los:
```
docker-compose run --rm app sh -c "python manage.py test && flake8"
```
Este comando é utilizado pelo travis-ci após cada `push` ao repositório.
