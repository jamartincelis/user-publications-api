from os import environ
import sys

import pendulum
import requests
from django.conf import settings

months_dict = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre',
}


def validate_date(value):
    try:
        value = value.split('-')
        return pendulum.datetime(int(value[0]), int(value[1]), 1, tz=environ.get('TIME_ZONE'))
    except (ValueError, TypeError, AttributeError):
        return False


def catalog_to_dict(catalogs_name):
    """
    Consulta un catálogo y lo convierte a diccionario para simular un 
    sistema de cache propio del proyecto y evitar consultas http masivas
    """
    data = {}
    for catalog_name in catalogs_name.split(','):
        for item in settings.TRANSACTION_CATEGORIES[catalog_name]:
            data[item['id']] = item
    return data

def get_catalog(catalog_name):
    """
    Realiza una consulta al microservicio de catálogos y obtiene la información
    necesaria de un catálogo. Sirve para inicializar widgets que requieran de catálogos
    """
    try:
        catalog_url = environ.get('CATALOG_SERVICE_URL')
        r = requests.get(catalog_url+'?catalog={}'.format(catalog_name), timeout=15)
        if r.status_code == 200:
            print('Catalog {} Loaded'.format(catalog_name).upper())
            return r.json()
        raise Exception('Failed to load catalog {}'.format(catalog_name).upper())
    except requests.exceptions.RequestException:
        raise Exception('Failed to load catalog {}'.format(catalog_name).upper())
