# Weather app

Endpoints App de clima api.

## Obtener el clima de las ciudades.

```bash
curl -X 'GET' \
  'http://localhost:8000/api/weather/cities' \
  -H 'accept: application/json'
```

respuesta

```json
[
    {
        "city": [
            "Medellín"
        ],
        "temperature": [
            292.77
        ],
        "description": [
            "Drizzle"
        ]
    },
    {
        "city": [
            "Caracas"
        ],
        "temperature": [
            292.7
        ],
        "description": [
            "Clouds"
        ]
    }
]
```
## Crear la ciudad.

```bash
curl -X 'POST' \
  'http://localhost:8000/api/weather/cities' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Medellín"
}'
```

respuesta

```json
{
    "city": [
        "Medellín"
    ],
    "temperature": [
        285.72
    ],
    "description": [
        "Rain"
    ]
}
```