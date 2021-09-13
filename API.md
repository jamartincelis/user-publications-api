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

## Obtener la lista de presupuestos del usuario

```bash
curl --request GET \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/budgets/
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

## Obtener un presupuesto del usuario

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

## Obtener la lista de todas las transacciones del usuario.


```bash
curl --request GET \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/transactions/
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
## Obtener las transacciones del usuario filtradas por categoría.

```bash
curl --request GET \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/transactions/categories/22118f55-e6a9-46b0-ae8f-a063dda396e0/
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

## Obtener una transaccion del usuario

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
