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
    """Recibe un valor date_month tipo string con el formato 2022-05 y regresa un objeto date."""
    # recibimos como queryparam un valor date_month con el formato 2022-01
    # tenemos que validar que el dato se pueda convertir a un tipo fecha
    # para filtrar las transacciones y presupuestos por mes
    try:
        value = value.split('-')
        return pendulum.datetime(int(value[0]), int(value[1]), 1, tz=environ.get('TIME_ZONE'))
    except (ValueError, TypeError, AttributeError):
        return False
