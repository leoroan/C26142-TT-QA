import pytest
import requests

LOGIN_URL = 'https://reqres.in/api/login'

HEADERS = {'x-api-key': 'free_user_3EaQQW9vs5jP7F7G5wSseMKrTEe'} # lo necesité para que no me tire 403..q ahroa me pedia cuenta

CASOS_LOGIN = [
    ({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 200, True),  # Válido
    ({"email": "eve.holt@reqres.in"}, 400, False)                            # Inválido (sin password)
]

@pytest.mark.api
@pytest.mark.parametrize("payload, status_esperado, debe_tener_token", CASOS_LOGIN)
def test_login_api(payload, status_esperado, debe_tener_token):
    """Valida el endpoint de login con casos de éxito y fallo"""
    
    response = requests.post(LOGIN_URL, json=payload, headers=HEADERS)
    
    # 1. Valido el Status Code
    assert response.status_code == status_esperado
    
    # 2. Valido la estructura de respuesta, si corresponde
    if debe_tener_token:
        assert 'token' in response.json()
