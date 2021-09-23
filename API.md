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

## Balance Mensual del usuario. 

```bash
curl --request GET \
  --url 'http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/transactions/balance/?year=2021'
```
respuesta

```json
[
    {
        "month_name": "January",
        "incomes": 2000,
        "expenses": -2300,
        "balance": -300,
        "year": "2021"
    },
    {
        "month_name": "February",
        "incomes": 2400,
        "expenses": 0,
        "balance": 2400,
        "year": "2021"
    },
    {
        "month_name": "March",
        "incomes": 2100,
        "expenses": 0,
        "balance": 2100,
        "year": "2021"
    },
    {
        "month_name": "April",
        "incomes": 25000,
        "expenses": -700,
        "balance": 24300,
        "year": "2021"
    },
    {
        "month_name": "May",
        "incomes": 210000,
        "expenses": -17000,
        "balance": 193000,
        "year": "2021"
    },
    {
        "month_name": "June",
        "incomes": 1100,
        "expenses": -170000,
        "balance": -168900,
        "year": "2021"
    },
    {
        "month_name": "July",
        "incomes": 21007,
        "expenses": -17002,
        "balance": 4005,
        "year": "2021"
    },
    {
        "month_name": "August",
        "incomes": 1005,
        "expenses": -700,
        "balance": 305,
        "year": "2021"
    },
    {
        "month_name": "September",
        "incomes": 2500,
        "expenses": -2580,
        "balance": -80,
        "year": "2021"
    },
    {
        "month_name": "October",
        "incomes": 7100,
        "expenses": -200,
        "balance": 6900,
        "year": "2021"
    },
    {
        "month_name": "November",
        "incomes": 2105,
        "expenses": -800,
        "balance": 1305,
        "year": "2021"
    },
    {
        "month_name": "December",
        "incomes": 2100,
        "expenses": -1800,
        "balance": 300,
        "year": "2021"
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
## resumen de egresos y presupuestos por categoría..

```bash
curl --request GET \
  --url 'http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/transactions/expenses/summary/?date_month=2021-09'
```

  respuesta

```json
[
    {
        "category": "Entretenimiento",
        "spend": 29880.0,
        "movements": 3,
        "percentage": 50.75
    },
    {
        "category": "Shopping",
        "spend": 29000.0,
        "movements": 3,
        "percentage": 49.25
    }
]
```
