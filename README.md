# Project name

User publications api.

# Version 

Versión en desarrollo v.0.1

## Description

Desarrollo de endpoints para la app de publicaciones de usuarios.

## Requirements and Installation

Se pueden ver en el archivo requirements.txt.

## Ejecutar la app

```bash
docker-compose build
```

luego

```bash
docker-compose up
```

## Ejecutar las migraciones

```bash
docker exec -it flask-app sh
```

y luego 

```bash
flask db upgrade
```

## Ejecutar las pruebas unitarias

```bash
docker exec -it weather-app sh

```

luego

```bash
pytest
```
