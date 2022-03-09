# Djang-Api-Rest-Rastreamento-IP

Construção de um API Rest, que tem como objetivo de receber um IP e retornar as suas informações, como sua localidade, região e país.

Para a inicialização do desafio será necessário, baixar os importes do requirements.txt, como também fazer as migrations e criar um usuário.

Após rodar o desafio, você terá duas opções de endpoint.

1. Endpoint **ip** que irão criar a requisição e salvar o ip no banco de dados. **[http://127.0.0.1:8000/api/v1/ip/**](http://127.0.0.1:8000/api/v1/ips/)
1. Endpoint, e o **ips** que irá listar todos os ips criados. [**http://127.0.0.1:8000/api/v1/ips/**](http://127.0.0.1:8000/api/v1/ips/)

Exemplo IPs:

- 230.76.84.206 - (Invalido)
- 76.109.221.174
- 20.39.101.124
- 215.227.43.31
- 71.1.225.9

Exemplo json para endpoint IP:

{ “ip”:”71.1.225.9” }

Testes

Para a criação dos testes, utilizei o pytest para melhorar a visualização, model-bakery para facilitar os teste na model e o coverage para auxiliar no que precisa ser testado e o que foi testado.
