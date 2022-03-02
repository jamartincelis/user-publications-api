# Coopeuch Salud Financiera

Endpoints del proyecto coopeuch salud financiera.

## Obtener los presupuestos del usuario filtrados por mes.

```bash
curl -X 'GET' \
  'http://localhost:8000/pfm-service/user/479ec168013945d0b7042bc4e5d0c4fb/budgets/?date_month=2021-09' \
  -H 'accept: application/json'
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
curl -X 'GET' \
  'http://localhost:8000/pfm-service/user/479ec168013945d0b7042bc4e5d0c4fb/budgets/categories/22118f55-e6a9-46b0-ae8f-a063dda396e0/?date_month=2021-09' \
  -H 'accept: application/json'
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
curl -X 'GET' \
  'http://localhost:8000/pfm-service/user/479ec168013945d0b7042bc4e5d0c4fb/budgets/45a80dbbea714ce390b3-6761bcbf365c/' \
  -H 'accept: application/json'
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
## Crear presupuesto (revisar presupuestos). 

```bash
curl -X 'POST' \
  'http://localhost:8000/pfm-service/user/479ec168013945d0b7042bc4e5d0c4fb/budgets/' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "amount": 9000,
  "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb",
  "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"
}'
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

## Editar el presupuesto del usuario.

Forma 1

```bash
curl -X 'PATCH' \
  'http://localhost:8000/pfm-service/user/479ec168013945d0b7042bc4e5d0c4fb/budgets/45a80dbbea714ce390b3-6761bcbf365c/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "amount": 9000
}'
```
respuesta 

```json
{
  "id": "45a80dbb-ea71-4ce3-90b3-6761bcbf365c",
  "amount": "5100.00",
  "expenses_sum": "1000.00",
  "expenses_count": 2,
  "average": "500.00",
  "spent": "20.0",
  "budget_date": "2021-09-09",
  "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb",
  "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"
}
```
Forma 2

```bash
curl -X 'PUT' \
  'http://localhost:8000/pfm-service/user/479ec168013945d0b7042bc4e5d0c4fb/budgets/45a80dbbea714ce390b3-6761bcbf365c/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user": "479ec168013945d0b7042bc4e5d0c4fb",
  "amount": 10000,
  "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"
}'
```
respuesta 

```json
{
  "id": "45a80dbb-ea71-4ce3-90b3-6761bcbf365c",
  "amount": "5100.00",
  "expenses_sum": "1100.00",
  "expenses_count": 3,
  "average": "450.00",
  "spent": "20.0",
  "budget_date": "2021-09-09",
  "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb",
  "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"
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
        "year": 2021,
        "months": [
            {
                "year": 2021,
                "month": "Enero",
                "incomes": 2000.0,
                "expenses": -2300.0,
                "balance": -300.0,
                "disabled": false
            },
            {
                "year": 2021,
                "month": "Febrero",
                "incomes": 2400.0,
                "expenses": 0.0,
                "balance": 2400.0,
                "disabled": true
            },
            {
                "year": 2021,
                "month": "Marzo",
                "incomes": 2100.0,
                "expenses": 0.0,
                "balance": 2100.0,
                "disabled": true
            },
            {
                "year": 2021,
                "month": "Abril",
                "incomes": 25000.0,
                "expenses": -700.0,
                "balance": 24300.0,
                "disabled": false
            },
            {
                "year": 2021,
                "month": "Mayo",
                "incomes": 210000.0,
                "expenses": -17000.0,
                "balance": 193000.0,
                "disabled": false
            },
            {
                "year": 2021,
                "month": "Junio",
                "incomes": 1100.0,
                "expenses": -170000.0,
                "balance": -168900.0,
                "disabled": false
            },
            {
                "year": 2021,
                "month": "Julio",
                "incomes": 21007.0,
                "expenses": -17002.0,
                "balance": 4005.0,
                "disabled": false
            },
            {
                "year": 2021,
                "month": "Agosto",
                "incomes": 1005.0,
                "expenses": -700.0,
                "balance": 305.0,
                "disabled": false
            },
            {
                "year": 2021,
                "month": "Septiembre",
                "incomes": 2500.0,
                "expenses": -58880.0,
                "balance": -56380.0,
                "disabled": false
            },
            {
                "year": 2021,
                "month": "Octubre",
                "incomes": 7100.0,
                "expenses": -200.0,
                "balance": 6900.0,
                "disabled": false
            },
            {
                "year": 2021,
                "month": "Noviembre",
                "incomes": 2105.0,
                "expenses": -800.0,
                "balance": 1305.0,
                "disabled": false
            },
            {
                "year": 2021,
                "month": "Diciembre",
                "incomes": 2100.0,
                "expenses": -1800.0,
                "balance": 300.0,
                "disabled": false
            }
        ]
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
## Resumen de egresos y presupuestos por categoría..

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

## Preguntas Frecuentes.

```bash
curl --request GET \
  --url http://localhost:8000/faqs/
```

  respuesta

```json
[
    {
        "id": 1,
        "question": "Pregunta 1",
        "answer": "Respuesta 1"
    },
    {
        "id": 2,
        "question": "Pregunta 2",
        "answer": "Respuesta 2"
    },
    {
        "id": 3,
        "question": "Pregunta 3",
        "answer": "Respuesta 3"
    },
    {
        "id": 4,
        "question": "Pregunta 4",
        "answer": "Respuesta 4"
    },
    {
        "id": 5,
        "question": "Pregunta 5",
        "answer": "Respuesta 5"
    },
    {
        "id": 6,
        "question": "Pregunta 6",
        "answer": "Respuesta 6"
    }
]
```

## Consejos.

```bash
curl --request GET \
  --url http://localhost:8000/tips/
```

  respuesta

```json
[
    {
        "id": 2,
        "name": "Consejo #1",
        "description": "Intenta mantener todos tus movimientos categorizados para que sepas dónde se va tu dinero. ¿Hay alguna categoría que no te hace sentido? Puedes editarla para tener todo bajo control.",
        "metadata": {
            "icon": "advice-1.svg"
        }
    },
    {
        "id": 3,
        "name": "Consejo #2",
        "description": "Los presupuestos te ayudan a fijar un límite de gasto en una categoría. Crea uno y define el monto máximo que quieres gastar en un mes. Revísalo de forma períodica para que controles mejor tus gastos.",
        "metadata": {
            "icon": "advice-1.svg"
        }
    },
    {
        "id": 4,
        "name": "Consejo #3",
        "description": "Usa tus tarjetas de débito Coopeuch para hacer todas tus compras, así tendrás una mirada completa de tu salud financiera en esta plataforma.",
        "metadata": {
            "icon": "advice-1.svg"
        }
    },
]
```

## Notifications.

```bash
curl --request GET \
  --url http://localhost:8000/notifications/
```

  respuesta

```json
[
    {
        "id": 1,
        "description": "<b>¡Inviete ya!</b> Te ayudaremos para que comiences a invertir tu dinero <a>aquí</a>",
        "metadata": {
            "icon": "assets/img/img_user.svg",
            "backgorund": "#FFFFFF"
        }
    },
    {
        "id": 2,
        "description": "<b>¡Muy bien!</b> Llevas un buen orden, te recomiendo <b>ahorrar</b> o <b>invertir</b> tu dinero. Conoce más consejos.",
        "metadata": {
            "icon": "assets/img/img_user.svg",
            "backgorund": "#e0e4f4"
        }
    }
]
```