# employee-register-service
Aplicação de serviço API Rest de cadastro de funcionários desenvolvida em Django.

# Routes

http://3.14.1.119/api/employee/create/
Requisição: POST

Route para o cadastro de funcionários, tem como campos obigatórios email, senha, nome e código postal brasileiro. Retorna um JSON com o email, nome, código postal e os campos endereço, bairro, cidade e estado - estes quatro últimos disponibilizados via consulta ao micro serviço.

Exemplo de requisição
- Entrada (form-data no body)
    email: joaosantos@gmail.com
    password: senha123
    name: João Santos
    postal_code: 09781250

- Saída (content-type application/json)
    {
        "email": "joaosantos@gmail.com",
        "name": "João Santos",
        "postal_code": "09781250",
        "address": "Rua Papa Paulo VI (Jd Yrajá)",
        "neighborhood": "Santa Terezinha",
        "city": "São Bernardo do Campo",
        "state": "SP"
    }
