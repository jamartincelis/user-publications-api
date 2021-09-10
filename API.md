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

## Obtener la lista de presupuestos

```bash
curl --request GET \
  --url http://localhost:8000/budget/
```

## Obtener la lista de transacciones

```bash
curl --request GET \
  --url http://localhost:8000/transaction/
```

## Obtener la lista de transacciones

```bash
curl --request GET \
  --url http://localhost:8000/user/
```