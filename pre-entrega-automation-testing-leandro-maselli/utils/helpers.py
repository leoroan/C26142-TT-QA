from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceHelpers:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        """Realiza el login y confirma que el botón de ingreso desaparezca."""
        print(f"\n[LOGIN] Intentando ingresar con usuario: {username}")
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    def obtener_primer_producto_y_validar(self):
        """Valida la presencia de productos y retorna datos del primero."""
        print("[CATÁLOGO] Validando presencia de productos en el inventario...")
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        
        # Validamos que la lista tenga contenido
        cantidad = len(items)
        assert cantidad > 0, f"Error: Se esperaban productos pero se encontraron {cantidad}"
        
        primer_item = items[0]
        nombre = primer_item.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = primer_item.find_element(By.CLASS_NAME, "inventory_item_price").text
        
        return primer_item, nombre, precio

    def verificar_presencia_componentes_criticos(self):
        """Valida que los elementos estructurales de la página estén visibles."""
        print("[UI] Verificando componentes críticos (Menú, Filtros, Carrito)...")
        componentes = {
            "Botón de Menú": (By.ID, "react-burger-menu-btn"),
            "Selector de Filtros": (By.CLASS_NAME, "product_sort_container"),
            "Icono del Carrito": (By.CLASS_NAME, "shopping_cart_link"),
            "Footer": (By.CLASS_NAME, "footer")
        }
        
        for nombre, locator in componentes.items():
            elemento = self.driver.find_element(*locator)
            assert elemento.is_displayed(), f"Error: El componente '{nombre}' no es visible."
        return True