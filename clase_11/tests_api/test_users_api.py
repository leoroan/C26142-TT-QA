import pytest
import requests

USERS_URL = 'https://reqres.in/api/users?page=1'

HEADERS = {'x-api-key': 'free_user_3EaQQW9vs5jP7F7G5wSseMKrTEe'}

@pytest.mark.api
def test_get_users():
    """Valida la lista de usuarios, las claves requeridas y el formato del avatar"""
    
    response = requests.get(USERS_URL, headers=HEADERS)
    assert response.status_code == 200
    
    data = response.json()
    usuarios = data['data']
    
    # Evitar procesar listas vacías
    assert len(usuarios) > 0 
    
    for usuario in usuarios:
        # Verificar que el usuario tenga las claves obligatorias
        claves_requeridas = {'id', 'email', 'first_name', 'last_name'}
        assert claves_requeridas <= set(usuario.keys())
        
        # Extra: Validar que el avatar termina en .jpg
        assert usuario['avatar'].endswith('.jpg')