import pytest
import requests
import time
from faker import Faker

fake = Faker()
BASE_URL = 'https://jsonplaceholder.typicode.com'

@pytest.mark.e2e
def test_post_lifecycle():
    """Validar el ciclo de vida completo de un recurso: POST, PATCH y DELETE."""
    
    # Iniciamos el temporizador global (El flujo completo debe ser < 3s según criterios de aceptación)
    start_time_total = time.time()

    # ==========================================
    # 1. POST - Crear recurso
    # ==========================================
    payload_post = {
        'title': fake.sentence(),
        'body': fake.text(),
        'userId': 1
    }
    
    start_post = time.time()
    response_post = requests.post(f"{BASE_URL}/posts", json=payload_post)
    tiempo_post = time.time() - start_post
    
    # Validaciones POST
    assert response_post.status_code == 201, "Error en la creación del recurso"
    assert tiempo_post < 1.5, "POST demasiado lento"
    
    body_post = response_post.json()
    
    # Validar esquema y tipos
    assert 'id' in body_post, "El esquema no contiene un ID"
    assert isinstance(body_post['id'], int), "El ID devuelto no es de tipo entero"
    assert isinstance(body_post['title'], str), "El title no es de tipo string"
    
    # Guardamos el ID generado
    post_id = body_post['id']
    print(f"\n[INFO] Recurso creado exitosamente con ID: {post_id}")

    # ==========================================
    # 2. PATCH - Actualizar recurso
    # ==========================================
    payload_patch = {
        'title': 'Título actualizado por QA'
    }
    
    start_patch = time.time()
    response_patch = requests.patch(f"{BASE_URL}/posts/{post_id}", json=payload_patch)
    tiempo_patch = time.time() - start_patch
    
    # Validaciones PATCH
    assert response_patch.status_code == 200, "Error al actualizar el recurso"
    assert tiempo_patch < 1.0, "PATCH demasiado lento"
    
    body_patch = response_patch.json()
    
    # Validar contenido actualizado y tipos
    assert body_patch['title'] == 'Título actualizado por QA', "El título no se actualizó correctamente"
    assert isinstance(body_patch['title'], str)
    print(f"[INFO] Título del recurso {post_id} actualizado mediante PATCH.")

    # ==========================================
    # 3. DELETE - Eliminar recurso
    # ==========================================
    start_delete = time.time()
    response_delete = requests.delete(f"{BASE_URL}/posts/{post_id}")
    tiempo_delete = time.time() - start_delete
    
    # Validaciones DELETE
    assert response_delete.status_code == 200, "Error al eliminar el recurso" # JSONPlaceholder devuelve 200
    assert tiempo_delete < 1.0, "DELETE demasiado lento"
    
    # Validar esquema vacío en la respuesta de eliminación
    body_delete = response_delete.json()
    assert body_delete == {}, "DELETE no devolvió un esquema vacío como se esperaba"
    
    print(f"[INFO] Recurso {post_id} eliminado exitosamente.")

    # ==========================================
    # 4. Validación Final de Tiempo (Requerimiento Jira)
    # ==========================================
    tiempo_total = time.time() - start_time_total
    assert tiempo_total < 3.0, f"El flujo completo demoró más de 3 segundos ({tiempo_total:.2f}s)"
    print(f"[INFO] Flujo E2E completado en {tiempo_total:.2f}s.")