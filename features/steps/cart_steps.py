from behave import given, when, then

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

from utils.logger import logger


@given("he iniciado sesión correctamente")
def step_login_ok(context):

    login = LoginPage(context.driver)

    login.abrir()

    login.login_completo(
        "standard_user",
        "secret_sauce"
    )

    context.inventory = InventoryPage(
        context.driver
    )

    logger.info(
        "Login realizado"
    )


@when("agrego el primer producto")
def step_agregar_producto(context):

    context.inventory.agregar_primer_producto()

    logger.info(
        "Producto agregado"
    )


@then("el contador del carrito muestra 1")
def step_validar_carrito(context):

    assert (
        context.inventory.obtener_contador_carrito()
        == 1
    )