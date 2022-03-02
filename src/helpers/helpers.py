from os import environ

import pendulum


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
        return pendulum.from_format(value+'-01', 'YYYY-MM-DD')
    except (ValueError, TypeError):
        return False

def catalog_to_dict(catalog_name):
    """
    Consulta un catálogo y lo convierte a diccionario para simular un sistema de cache propio del
    proyecto y evitar consultas http masivas
    """
    try:
        catalog_url = environ.get('CATALOG_SERVICE_URL')
        r = requests.get(catalog_url+'?catalog={}'.format(catalog_name)).json()
        data = {}
        for item in r[catalog_name]:
            data[item['id']] = item
        print('CATALOG DATA LOADED')
        return data
    except Exception:
        return {}

def get_catalog(catalog_name):
    """
    Realiza una consulta al microservicio de catálogos y obtiene la información
    necesaria de un catálogo. Sirve para inicializar widgets que requieran de catálogos
    """
    catalog_url = environ.get('CATALOG_SERVICE_URL')
    try:
        print('CATALOG DATA LOADED')
        return requests.get(catalog_url+'?catalog={}'.format(catalog_name)).json()
    except requests.exceptions.RequestException:
        return {}