# Coopeuch Salud Financiera

Endpoints del proyecto coopeuch salud financiera.

## Obtener la lista de catalogos

```bash
curl --request GET \
  --url http://localhost:8000/catalog/codes_list 
```

## Obtener la lista de tipos de catalogos

```bash
curl --request GET \
  --url http://localhost:8000/catalog/codetypes_list/
```

## Obtener la lista de catalogos con sus tipos de catalogos asociados

```bash
curl --request GET \
  --url http://localhost:8000/catalog/list/
```

## Obtener tipos de catalogos por nombre

```bash
curl --request GET \
  --url http://localhost:8000/catalog/{name}/
```

ejemplo

```bash
curl --request GET \
  --url http://localhost:8000/catalog/account_status/
```

## Acceder a los datos del usuario

```bash
curl --request GET \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/
```

respuesta

```json
{
    "id": "479ec168-0139-45d0-b704-2bc4e5d0c4fb",
    "optional_id": "479ec168013945d0b7042bc4e5d0c4fb",
    "email": "correo@correo.com"
}
```

## Obtener los presupuestos del usuario filtrados por mes.

```bash
curl --request GET \
  --url 'http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/budgets/?date_month=2021-09' \
```

respuesta

```json
[
    {
        "id": "45a80dbb-ea71-4ce3-90b3-6761bcbf365c",
        "category": {
            "id": "22118f55-e6a9-46b0-ae8f-a063dda396e0",
            "name": "shopping",
            "description": "Shopping",
            "metadata": {
                "icon": "icon.png"
            },
            "created_at": "2021-05-01T15:20:30-04:00",
            "updated_at": "2021-05-01T15:20:30-04:00",
            "code_type": "1ec6a6b5-65d5-4a8c-85d0-4364c141aefd"
        },
        "amount": "2400.00",
        "budget_date": "2021-09-09T15:20:30-04:00",
        "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb"
    }
]
```
## Obtener los presupuestos del usuario filtrados por categoría y por mes.

```bash
curl --request GET \
  --url 'http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/budgets/categories/22118f55-e6a9-46b0-ae8f-a063dda396e0/?date_month=2021-09' \
```

respuesta

```json
[
    {
        "id": "45a80dbb-ea71-4ce3-90b3-6761bcbf365c",
        "category": {
            "id": "22118f55-e6a9-46b0-ae8f-a063dda396e0",
            "name": "shopping",
            "description": "Shopping",
            "metadata": {
                "icon": "icon.png"
            },
            "created_at": "2021-05-01T15:20:30-04:00",
            "updated_at": "2021-05-01T15:20:30-04:00",
            "code_type": "1ec6a6b5-65d5-4a8c-85d0-4364c141aefd"
        },
        "amount": "2400.00",
        "budget_date": "2021-09-09T15:20:30-04:00",
        "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb"
    }
]
```

## Detalle del presupuesto del usuario.

```bash
curl --request GET \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/budgets/45a80dbbea714ce390b3-6761bcbf365c/
```
respuesta

```json
{
    "id": "45a80dbb-ea71-4ce3-90b3-6761bcbf365c",
    "category": {
        "id": "22118f55-e6a9-46b0-ae8f-a063dda396e0",
        "name": "shopping",
        "description": "Shopping",
        "metadata": {
            "icon": "icon.png"
        },
        "created_at": "2021-05-01T15:20:30-04:00",
        "updated_at": "2021-05-01T15:20:30-04:00",
        "code_type": "1ec6a6b5-65d5-4a8c-85d0-4364c141aefd"
    },
    "amount": "2400.00",
    "budget_date": "2021-09-09T15:20:30-04:00",
    "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb"
}
```
## Crear presupuesto. 

```bash
curl --request POST \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/budgets/ \
  --header 'content-type: application/json' \
  --data '{"amount": 3000,"budget_date": "2021-09-09T15:20:30-04:00","user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb","category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"}'
```
respuesta 

```json
{
  "id": "b4cb85bd-11e4-4ce7-9ef9-e0782cea58c1",
  "category": {
    "id": "22118f55-e6a9-46b0-ae8f-a063dda396e0",
    "name": "shopping",
    "description": "Shopping",
    "metadata": {
      "icon": "icon.png"
    },
    "created_at": "2021-05-01T15:20:30-04:00",
    "updated_at": "2021-05-01T15:20:30-04:00",
    "code_type": "1ec6a6b5-65d5-4a8c-85d0-4364c141aefd"
  },
  "amount": "3000.00",
  "budget_date": "2021-09-09T15:20:30-04:00",
  "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb"
}
```

## Obtener las transacciones del usuario filtradas por mes. 

```bash
curl --request GET \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/transactions/?date_month=2021-09
```

respuesta

```json
[
    {
        "id": "68e18783-8b51-4618-af83-50c77f25871d",
        "category": {
            "id": "22118f55-e6a9-46b0-ae8f-a063dda396e0",
            "name": "shopping",
            "description": "Shopping",
            "metadata": {
                "icon": "icon.png"
            },
            "created_at": "2021-05-01T15:20:30-04:00",
            "updated_at": "2021-05-01T15:20:30-04:00",
            "code_type": "1ec6a6b5-65d5-4a8c-85d0-4364c141aefd"
        },
        "amount": "1500.00",
        "description": "Transaccion de prueba 1",
        "transaction_date": "2021-09-09T15:20:30-04:00",
        "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb"
    }
]
```

## Obtener las transacciones del usuario filtradas por categoría y por mes.

```bash
curl --request GET \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/transactions/categories/22118f55-e6a9-46b0-ae8f-a063dda396e0/?date_month=2021-09
```

respuesta

```json
[
    {
        "id": "68e18783-8b51-4618-af83-50c77f25871d",
        "category": {
            "id": "22118f55-e6a9-46b0-ae8f-a063dda396e0",
            "name": "shopping",
            "description": "Shopping",
            "metadata": {
                "icon": "icon.png"
            },
            "created_at": "2021-05-01T15:20:30-04:00",
            "updated_at": "2021-05-01T15:20:30-04:00",
            "code_type": "1ec6a6b5-65d5-4a8c-85d0-4364c141aefd"
        },
        "amount": "1500.00",
        "description": "Transaccion de prueba 1",
        "transaction_date": "2021-09-09T15:20:30-04:00",
        "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb"
    }
]
```

## Asignar nota.

```bash
curl --request PATCH \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/transactions/68e18783-8b51-4618-af83-50c77f25871d/ \
  --header 'content-type: application/json' \
  --data '{"user_note" : "Transaccion de prueba 3"}'
```
respuesta

```json
{
  "id": "0b32a3b9-3396-4c19-b418-6236ab034a02",
  "amount": "8000.00",
  "description": "Prueba",
  "transaction_date": "2021-09-13T12:56:00-04:00",
  "user_note": "Transaccion de prueba 3",
  "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb",
  "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"
}
```
## Asignar categoría.

```bash
curl --request PATCH \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/transactions/0b32a3b9-3396-4c19-b418-6236ab034a02/ \
  --header 'content-type: application/json' \
  --data '{"category" : "22118f55-e6a9-46b0-ae8f-a063dda396e0"}'
```
respuesta

```json
{
  "id": "0b32a3b9-3396-4c19-b418-6236ab034a02",
  "amount": "8000.00",
  "description": "Prueba",
  "transaction_date": "2021-09-13T12:56:00-04:00",
  "user_note": "Transaccion de prueba 3",
  "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb",
  "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"
}
```

## Detalle de transaccion del usuario.

```bash
curl --request GET \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/transactions/68e18783-8b51-4618-af83-50c77f25871d/
```
respuesta

```json
{
    "id": "68e18783-8b51-4618-af83-50c77f25871d",
    "category": {
        "id": "22118f55-e6a9-46b0-ae8f-a063dda396e0",
        "name": "shopping",
        "description": "Shopping",
        "metadata": {
            "icon": "icon.png"
        },
        "created_at": "2021-05-01T15:20:30-04:00",
        "updated_at": "2021-05-01T15:20:30-04:00",
        "code_type": "1ec6a6b5-65d5-4a8c-85d0-4364c141aefd"
    },
    "amount": "1500.00",
    "description": "Transaccion de prueba 1",
    "transaction_date": "2021-09-09T15:20:30-04:00",
    "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb"
}
```
## Gasto total por categoría.

curl --request GET \
  --url 'http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/transactions/summary/?date_month=2021-09' \

  respuesta

```json
[
  {
    "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0",
    "total_spend": 9500,
    "num_transaction": 2
  },
  {
    "category": "9abd4759-ab14-4e09-adc2-9c5dea1041b1",
    "total_spend": 2000,
    "num_transaction": 2
  }
]
```