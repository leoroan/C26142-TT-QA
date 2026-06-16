import pytest

from selenium.webdriver.common.by import By

from utils.helpers import SauceHelpers
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
def test_compra_flujo_basico(driver):

    sauce = SauceHelpers(driver)

    logger.info("===== INICIO TEST UI =====")

    # =====================================================
    # LOGIN
    # =====================================================

    logger.info("Abriendo SauceDemo")

    driver.get(
        "https://www.saucedemo.com"
    )

    assert "Swag Labs" in driver.title

    logger.info("Realizando login")

    sauce.login(
        "standard_user",
        "secret_sauce"
    )

    logger.info("Validando redirección")

    assert "/inventory.html" in driver.current_url

    titulo_header = driver.find_element(
        By.CSS_SELECTOR,
        ".title"
    ).text

    assert titulo_header == "Products"

    # =====================================================
    # CATÁLOGO
    # =====================================================

    logger.info("Verificando catálogo")

    sauce.verificar_presencia_componentes_criticos()

    (
        item_elem,
        nombre_prod,
        precio_prod
    ) = sauce.obtener_primer_producto_y_validar()

    logger.info(
        f"Producto encontrado: {nombre_prod}"
    )

    assert nombre_prod

    assert "$" in precio_prod

    # =====================================================
    # CARRITO
    # =====================================================

    logger.info(
        f"Agregando producto al carrito: {nombre_prod}"
    )

    btn_add = item_elem.find_element(
        By.XPATH,
        ".//button[contains(@id,'add-to-cart')]"
    )

    btn_add.click()

    badge_elem = driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert badge_elem.text == "1"

    logger.info(
        "Badge actualizado correctamente"
    )

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    assert "/cart.html" in driver.current_url

    nombre_en_carrito = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    assert nombre_en_carrito == nombre_prod

    logger.info(
        f"Producto validado en carrito: {nombre_en_carrito}"
    )

    logger.info(
        "===== FIN TEST UI ====="
    )