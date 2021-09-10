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

## Obtener la lista de presupuestos del usuario

```bash
curl --request GET \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/budget/
```

respuesta

```json
[
    {
        "id": "45a80dbb-ea71-4ce3-90b3-6761bcbf365c",
        "budget_date": "2021-09-09T15:20:30-04:00",
        "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb",
        "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"
    }
]
```

## Obtener un presupuesto del usuario

```bash
curl --request GET \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/budget/45a80dbbea714ce390b3-6761bcbf365c/
```
respuesta

```json
{
    "id": "45a80dbb-ea71-4ce3-90b3-6761bcbf365c",
    "budget_date": "2021-09-09T15:20:30-04:00",
    "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb",
    "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"
}
```

## Obtener la lista de transacciones del usuario


```bash
curl --request GET \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/transaction/
```

respuesta

```json
[
    {
        "id": "68e18783-8b51-4618-af83-50c77f25871d",
        "amount": "1500.00",
        "description": "Transaccion de prueba 2",
        "transaction_date": "2021-09-09T15:20:30-04:00",
        "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb",
        "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"
    }
]
```

## Obtener una transaccion del usuario

```bash
curl --request GET \
  --url http://localhost:8000/user/479ec168013945d0b7042bc4e5d0c4fb/transaction/68e18783-8b51-4618-af83-50c77f25871d/
```
respuesta

```json
{
    "id": "68e18783-8b51-4618-af83-50c77f25871d",
    "amount": "1500.00",
    "description": "Transaccion de prueba 2",
    "transaction_date": "2021-09-09T15:20:30-04:00",
    "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb",
    "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"
}
```