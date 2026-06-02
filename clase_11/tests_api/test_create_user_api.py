import pytest
import requests
from datetime import datetime

CREATE_URL = 'https://reqres.in/api/users'

HEADERS = {'x-api-key': 'free_user_3EaQQW9vs5jP7F7G5wSseMKrTEe'}

# Datos parametrizados para la creación
NUEVOS_USUARIOS = [
    {'name': 'Matias QA', 'job': 'tester'},
    {'name': 'Silvia PO', 'job': 'product_owner'},
    {'name': 'Neo', 'job': 'the_one'}
]

@pytest.mark.api
@pytest.mark.parametrize("payload", NUEVOS_USUARIOS)
def test_create_user(payload):
    """Valida la creación de nuevos recursos mediante POST"""
    
    response = requests.post(CREATE_URL, json=payload, headers=HEADERS)
    
    # 1. Validar Status 201 (Created)
    assert response.status_code == 201
    
    new_user = response.json()
    
    # 2. Validar que la respuesta contiene los datos enviados
    assert new_user['name'] == payload['name']
    assert new_user['job'] == payload['job']
    
    # 3. Validar que createdAt incluye el año actual
    año_actual = str(datetime.now().year)
    assert año_actual in new_user['createdAt']