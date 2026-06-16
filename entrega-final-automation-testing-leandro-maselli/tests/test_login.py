from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_exitoso(driver):
    # 1. Instanciamos la página de login
    login_page = LoginPage(driver)
    
    # 2. Ejecutamos las acciones usando los métodos encadenados
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    
    # 3. Instanciamos la página de inventario y hacemos los asserts (validaciones)
    inventory_page = InventoryPage(driver)
    assert inventory_page.obtener_titulo() == "Products"