from json import dumps

def test_login(test_client):
    payload = {
        "username": "johnsmith@correo.com",
        "password": "123456"      
    }

    response = test_client.post('/api/users/login',
        data=dumps(payload),
        content_type='application/json'
    )
    assert response.status_code == 200