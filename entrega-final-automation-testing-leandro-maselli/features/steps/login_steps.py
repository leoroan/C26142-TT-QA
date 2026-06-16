from behave import given, when, then

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

from utils.logger import logger


@given("estoy en la página de login")
def step_login_page(context):

    logger.info("Abriendo login")

    context.login_page = LoginPage(context.driver)

    context.login_page.abrir()


@when('ingreso usuario "{usuario}" y contraseña "{clave}"')
def step_ingresar_credenciales(
    context,
    usuario,
    clave
):

    logger.info(
        f"Login con usuario {usuario}"
    )

    context.login_page.login_completo(
        usuario,
        clave
    )

@when("intento iniciar sesión sin credenciales")
def step_login_vacio(context):

    context.login_page.login_completo(
        "",
        ""
    )

@then("debería ver la página de inventario")
def step_validar_inventory(context):

    inventory = InventoryPage(context.driver)

    assert (
        inventory.obtener_titulo()
        == "Products"
    )


@then("debería ver un mensaje de error")
def step_error(context):

    print(
        context.login_page.obtener_mensaje_error()
    )

    assert (
        context.login_page.esta_error_visible()
    )