import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.datos import leer_json_productos

# 1. Cargamos los datos leyendo el archivo JSON externo
PRODUCTOS = leer_json_productos('datos/productos.json')

# 2. Fixture para evitar repetir el login en cada test
@pytest.fixture
def usuario_logueado(driver):
    """Fixture que realiza login antes de cada test de carrito."""
    print("\n[PRE-CONDICIÓN] Iniciando sesión para interactuar con el carrito...")
    login_page = LoginPage(driver)
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    
    # Devolvemos el driver ya posicionado en la página de inventario
    return driver

# 3. Parametrización: Inyectamos cada diccionario del JSON en el test
@pytest.mark.parametrize("producto", PRODUCTOS)
def test_agregar_producto_desde_json(usuario_logueado, producto):
    """Test que agrega cada producto del JSON al carrito."""
    
    driver = usuario_logueado
    
    # Extraemos los datos específicos del diccionario que nos manda el JSON
    nombre_producto = producto["nombre"]
    xpath_boton = producto["xpath_add_button"]
    
    print(f"\n[INFO] Validando agregado al carrito del producto: {nombre_producto}")
    
    # Hacemos clic en el botón de agregar al carrito utilizando el XPath del JSON
    driver.find_element(By.XPATH, xpath_boton).click()
    
    # Validamos que el icono del carrito muestre que se agregó 1 producto
    badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge_carrito == "1", f"Error: No se actualizó el contador al agregar {nombre_producto}"


# 4. Test de Smoke (Validación rápida)
@pytest.mark.smoke
def test_carrito_smoke(usuario_logueado):
    """Test de smoke que verifica funcionalidad básica del carrito."""
    
    driver = usuario_logueado
    print("\n[INFO] Ejecutando Smoke Test: Agregar y revisar carrito...")
    
    # Usamos la clase InventoryPage (POM) para agregar el primer producto genérico
    inventory_page = InventoryPage(driver)
    inventory_page.agregar_primer_producto()
    
    # Ingresamos al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Usamos la clase CartPage (POM) para validar que haya productos listados
    cart_page = CartPage(driver)
    lista_productos = cart_page.obtener_productos_en_carrito()
    
    assert len(lista_productos) > 0, "Error: El carrito está vacío en el Smoke Test."