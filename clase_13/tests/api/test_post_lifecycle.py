import time
import requests
import pytest
import pytest_check as check

from faker import Faker
from utils.logger import logger

fake = Faker()

BASE_URL = "https://jsonplaceholder.typicode.com"

MAX_POST_TIME = 2.5
MAX_PATCH_TIME = 1.0
MAX_DELETE_TIME = 1.0
MAX_TOTAL_TIME = 3.0


@pytest.mark.api
@pytest.mark.e2e
@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_post_lifecycle():
    """
    Validar ciclo completo:
    POST -> PATCH -> DELETE
    """

    logger.info("===== INICIO TEST POST LIFECYCLE =====")

    start_total = time.perf_counter()

    # =====================================================
    # POST
    # =====================================================

    payload_post = {
        "title": fake.sentence(),
        "body": fake.text(),
        "userId": 1,
    }

    logger.info("Creando recurso")

    start = time.perf_counter()

    response_post = requests.post(
        f"{BASE_URL}/posts",
        json=payload_post,
    )

    elapsed_post = time.perf_counter() - start

    body_post = response_post.json()

    check.equal(
        response_post.status_code,
        201,
        "POST debería devolver 201"
    )

    check.is_true(
        elapsed_post < MAX_POST_TIME,
        f"POST demoró {elapsed_post:.2f}s"
    )

    check.is_in(
        "id",
        body_post,
        "Respuesta POST sin id"
    )

    post_id = body_post.get("id")

    logger.info(
        f"POST OK | id={post_id} | tiempo={elapsed_post:.2f}s"
    )

    # =====================================================
    # PATCH
    # =====================================================

    payload_patch = {
        "title": "Título actualizado por QA"
    }

    logger.info(f"Actualizando recurso {post_id}")

    start = time.perf_counter()

    response_patch = requests.patch(
        f"{BASE_URL}/posts/{post_id}",
        json=payload_patch,
    )

    elapsed_patch = time.perf_counter() - start

    body_patch = response_patch.json()

    check.equal(
        response_patch.status_code,
        200,
        "PATCH debería devolver 200"
    )

    check.equal(
        body_patch["title"],
        payload_patch["title"],
        "PATCH no actualizó el título"
    )

    check.is_true(
        elapsed_patch < MAX_PATCH_TIME,
        f"PATCH demoró {elapsed_patch:.2f}s"
    )

    logger.info(
        f"PATCH OK | tiempo={elapsed_patch:.2f}s"
    )

    # =====================================================
    # DELETE
    # =====================================================

    logger.info(f"Eliminando recurso {post_id}")

    start = time.perf_counter()

    response_delete = requests.delete(
        f"{BASE_URL}/posts/{post_id}"
    )

    elapsed_delete = time.perf_counter() - start

    check.equal(
        response_delete.status_code,
        200,
        "DELETE debería devolver 200"
    )

    check.equal(
        response_delete.json(),
        {},
        "DELETE debería devolver {}"
    )

    check.is_true(
        elapsed_delete < MAX_DELETE_TIME,
        f"DELETE demoró {elapsed_delete:.2f}s"
    )

    logger.info(
        f"DELETE OK | tiempo={elapsed_delete:.2f}s"
    )

    # =====================================================
    # TIEMPO TOTAL
    # =====================================================

    total = time.perf_counter() - start_total

    check.is_true(
        total < MAX_TOTAL_TIME,
        f"Flujo completo demoró {total:.2f}s"
    )

    logger.info(
        f"===== FIN TEST ({total:.2f}s) ====="
    )