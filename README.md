# Project name

Coopeuch Salud Financiera

# Version 

Versión en desarrollo v.0.133

## Description

Desarrollo de endpoints para el proyecto coopeuch salud financiera.

## Requirements and Installation

Se pueden ver en el archivo common.txt y requeriments-dev.txt.

## Build

Para el ambiente de desarrollo

```bash
docker-compose -f local.yaml build
```

Para producción

```bash
docker-compose up
```

## Development Run

```bash
docker-compose -f local.yaml up
```

## Production Run

```bash
docker-compose up
```

### Api Rest Docs

Los enpoints se encuentran publicados en http://ec2-54-144-77-35.compute-1.amazonaws.com/. En el siguiente apartado, se puede ver la documentación de la api.

[Coopeuch Salud Financiera Api](API.md)

### Tech docs

#### Crear un usuario de pruebas. 

Una vez que al contenedor esté desplegado, ejecutar:

```bash
docker exec -it pfm_api python manage.py createsuperuser
```

#### AWS ec2:
```54.144.77.35```
```Llave: ubankpilotos```
