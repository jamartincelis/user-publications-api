from os import environ

import requests


def validate_user_accounts(data):
    core_url = environ.get('CORE_SERVICE_URL')
    response = requests.get(self.core_url+'accounts/?number={}'.format(account_number), timeout=1)
    if response.status_code == 200:
        return response.json()
    except requests.exceptions.RequestException:
        return False
    return False
