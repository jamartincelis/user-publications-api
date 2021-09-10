# Coopeuch Salud Financiera

Desarrollo de endpoints para el proyecto coopeuch salud financiera.

## Desplegar el proyecto en local

```bash
docker-compose -f local.yaml up
```

## Desplegar el proyecto en la instancia aws

```bash
docker-compose up
```

## Crear un usuario de pruebas

Una vez que al contenedor esté desplegado, ejecutar:

```bash
docker exec -it pfm_api python manage.py createsuperuser
```

## Coopeuch Salud Financiera Api

En el siguiente apartado, se puede ver la documentación de la api.

[Coopeuch Salud Financiera Api](API.md)