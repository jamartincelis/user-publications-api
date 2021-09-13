from os import environ
import pendulum
import pendulum.parsing.exceptions

def validate_date(value):
    try:
        return pendulum.parse(value+'-01', tz=environ.get('TIME_ZONE'))
    except pendulum.parsing.exceptions.ParserError:
        return False