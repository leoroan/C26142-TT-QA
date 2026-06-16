from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_verificar_catalogo_productos(driver):
    """Prueba que valida la presencia de productos en el catálogo tras hacer login."""
    
    # iniciamos sesión para llegar al inventario
    login_page = LoginPage(driver)
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    
    # Instanciamos la página del inventario
    inventory_page = InventoryPage(driver)
    
    print("\n[CATÁLOGO] Validando presencia de productos en el inventario...")
    
    # Validamos el título usando el método de la página
    assert inventory_page.obtener_titulo() == "Products", "Error: El título no es Products"
    
    # Obtenemos los productos y validamos que la lista tenga contenido
    productos = inventory_page.obtener_productos()
    cantidad = len(productos)
    assert cantidad > 0, f"Error: Se esperaban productos pero se encontraron {cantidad}"
    
    print(f"[CATÁLOGO] Validación exitosa. Se encontraron {cantidad} productos.")