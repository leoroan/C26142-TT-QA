import pytest
import requests
import time
from faker import Faker
import pytest_check as check  
from utils.logger import logger  

fake = Faker()
BASE_URL = 'https://jsonplaceholder.typicode.com'

@pytest.mark.e2e
@pytest.mark.flaky(reruns=2, reruns_delay=2) 
def test_post_lifecycle():
    """Validar el ciclo de vida completo de un recurso: POST, PATCH y DELETE."""
    
    logger.info("Iniciando flujo E2E: POST, PATCH y DELETE")
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
    
    check.equal(response_post.status_code, 201, "Error en la creación del recurso")
    check.is_true(tiempo_post < 2.5, f"POST demasiado lento: {tiempo_post:.2f}s")
    
    body_post = response_post.json()
    check.is_in('id', body_post, "El esquema no contiene un ID")
    
    post_id = body_post.get('id', 0)
    logger.info(f"Recurso creado exitosamente con ID: {post_id}")

    # ==========================================
    # 2. PATCH - Actualizar recurso
    # ==========================================
    payload_patch = {
        'title': 'Título actualizado por QA'
    }
    
    start_patch = time.time()
    response_patch = requests.patch(f"{BASE_URL}/posts/{post_id}", json=payload_patch)
    tiempo_patch = time.time() - start_patch
    
    check.equal(response_patch.status_code, 200, "Error al actualizar el recurso")
    check.is_true(tiempo_patch < 1.0, f"PATCH demasiado lento: {tiempo_patch:.2f}s")
    
    body_patch = response_patch.json()
    check.equal(body_patch.get('title'), 'Título actualizado por QA', "El título no se actualizó correctamente")
    logger.info(f"Título del recurso {post_id} actualizado mediante PATCH.")

    # ==========================================
    # 3. DELETE - Eliminar recurso
    # ==========================================
    start_delete = time.time()
    response_delete = requests.delete(f"{BASE_URL}/posts/{post_id}")
    tiempo_delete = time.time() - start_delete
    
    check.equal(response_delete.status_code, 200, "Error al eliminar el recurso")
    check.is_true(tiempo_delete < 1.0, f"DELETE demasiado lento: {tiempo_delete:.2f}s")
    
    body_delete = response_delete.json()
    check.equal(body_delete, {}, "DELETE no devolvió un esquema vacío como se esperaba")
    logger.info(f"Recurso {post_id} eliminado exitosamente.")

    # ==========================================
    # 4. Validación Final de Tiempo
    # ==========================================
    tiempo_total = time.time() - start_time_total
    check.is_true(tiempo_total < 3.0, f"El flujo completo demoró más de 3 segundos ({tiempo_total:.2f}s)")
    logger.info(f"Flujo E2E completado en {tiempo_total:.2f}s.")
    
