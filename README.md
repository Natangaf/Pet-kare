# PetKare API

Esta é a documentação da API PetKare, desenvolvida para o gerenciamento de dados de animais de estimação em petshops. A API permite cadastrar, listar, filtrar, atualizar e excluir informações sobre os pets dos clientes do PetKare. A documentação abaixo descreve as rotas disponíveis, seus verbos HTTP e os objetivos de cada uma.  

`POST /api/pets/`


## Esta rota é utilizada para cadastrar um novo pet. O corpo da requisição deve conter os dados do pet a ser cadastrado. Exemplo de requisição:

```json
{
  "nome": "Bob",
  "idade": 3,
  "raca": "Labrador",
  "dono": 1,
  "caracteristicas": [1, 2]
}
```


## Listar seleções

`GET /api/pets/`

Esta rota retorna a lista de todos os pets cadastrados. Exemplo de resposta:

```json
[
  {
    "id": 1,
    "nome": "Bob",
    "idade": 3,
    "raca": "Labrador",
    "dono": "João",
    "caracteristicas": [
      "Peludo",
      "Amigável"
    ]
  },
  {
    "id": 2,
    "nome": "Rex",
    "idade": 5,
    "raca": "Poodle",
    "dono": "Maria",
    "caracteristicas": [
      "Pequeno",
      "Brincalhão"
    ]
  }
]

```

## Filtragem de pet

`GET /api/pets/<pet_id>/`

Esta rota retorna os detalhes de um pet específico com base no seu ID. Substitua <pet_id> pelo ID do pet desejado. Exemplo de resposta:

```json
{
  "id": 1,
  "nome": "Bob",
  "idade": 3,
  "raca": "Labrador",
  "dono": "João",
  "caracteristicas": [
    "Peludo",
    "Amigável"
  ]
}

```

## Atualização de pet

`PATCH /api/pets/<pet_id>/`

Esta rota é utilizada para atualizar as informações de um pet específico. Substitua <pet_id> pelo ID do pet a ser atualizado. O corpo da requisição deve conter os dados atualizados do pet. Exemplo de requisição:

```json
{
  "idade": 4
}
```

## Deleção de pet

`DELETE /api/pets/<pet_id>/`

Esta rota é utilizada para excluir um pet específico com base no seu ID. Substitua <pet_id> pelo ID do pet a ser excluído.

Tratamento de exceção
A API PetKare possui tratamento de exceção nas rotas de criação, atualização, filtragem e deleção. Em caso de erros, serão retornadas respostas com o status HTTP apropriado e uma mensagem de erro detalhada.

Considerações finais
Esta documentação fornece uma visão geral das principais funcionalidades da API PetKare. Certifique-se de ler e entender os requisitos detalhados fornecidos para cada tarefa a ser desenvolvida ao longo do projeto. Em caso de dúvidas, consulte a equipe responsável pelo projeto.
