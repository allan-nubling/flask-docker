# flask-docker

## Sobre:

Este projeto visa o deployment de um modelo simples de (NLP) usando o scikit learn.

### O modelo
O modelo já foi treinado anteriormente e salvo usando a lib "joblib", é um modelo simples de categorização
utilizando regressão linear que categoriza produtos de acordo com algumas cetegorias já definidas no modelo.

O dataset utilizado para criação tem poucas entradas então não é um modelo muito bom.

## Como Usar:

Tenha certeza que você possui o Docker e Docker Compose(>=1.27.4) instalados.

- Crie /.env igual o /.env.example

```sh
- run docker-compose up -d
```

### Exemplo de requisição
```sh
curl --location --request POST 'localhost:5050/predict'
--header 'Content-Type: application/json'
```
```json
{
    "texts_snippets": [
        "farinha",
        "banana",
        "sabão"
    ]
}
```

### Resposta esperada

```json
{
    "prediction": [
        {
            "categorie": "Mercearia",
            "text": "farinha"
        },
        {
            "categorie": "Hortifruti",
            "text": "banana"
        },
        {
            "categorie": "Limpeza",
            "text": "sabão"
        }
    ]
}
```
