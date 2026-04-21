import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.helpers import SauceHelpers

@pytest.fixture
def driver():
    """Configuración simplificada con Selenium Manager."""
    driver = webdriver.Chrome() 
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_compra_flujo_basico(driver):
    sauce = SauceHelpers(driver)
    
    # --- PASO 1: NAVEGACIÓN Y LOGIN ---
    print("\n--- INICIANDO FASE 1: AUTENTICACIÓN ---")
    driver.get("https://www.saucedemo.com")
    
    # Validamos que estamos en la página de login antes de interactuar
    assert "Swag Labs" in driver.title, "No se pudo cargar la página de inicio"
    
    sauce.login("standard_user", "secret_sauce")
    
    # Validaciones específicas de redirección
    print("[CHECK] Validando redirección post-login...")
    assert "/inventory.html" in driver.current_url, f"URL incorrecta tras login: {driver.current_url}"
    
    titulo_header = driver.find_element(By.CSS_SELECTOR, ".title").text
    assert titulo_header == "Products", f"Se esperaba 'Products' pero se obtuvo '{titulo_header}'"

    # --- PASO 2: VERIFICACIÓN DEL CATÁLOGO ---
    print("\n--- INICIANDO FASE 2: VERIFICACIÓN DEL CATÁLOGO ---")
    
    # Validación de interfaz robusta
    sauce.verificar_presencia_componentes_criticos()
    
    # Validación de contenido de productos
    item_elem, nombre_prod, precio_prod = sauce.obtener_primer_producto_y_validar()
    print(f"[CHECK] Producto detectado: '{nombre_prod}' | Precio: {precio_prod}")
    
    assert len(nombre_prod) > 0, "El nombre del producto no puede estar vacío"
    assert "$" in precio_prod, "El formato del precio es incorrecto (falta símbolo $)"

    # --- PASO 3: INTERACCIÓN CON CARRITO ---
    print("\n--- INICIANDO FASE 3: GESTIÓN DEL CARRITO ---")
    
    # Acción: Añadir al carrito
    btn_add = item_elem.find_element(By.XPATH, ".//button[contains(@id,'add-to-cart')]")
    btn_add.click()
    print(f"[ACCIÓN] Se hizo clic en 'Add to cart' para: {nombre_prod}")
    
    # Validación específica del contador (Badge)
    badge_elem = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge_elem.text == "1", f"El contador muestra {badge_elem.text}, se esperaba 1."
    print(f"[CHECK] Badge del carrito actualizado correctamente: {badge_elem.text}")

    # Navegación al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Verificación final de integridad del producto
    print("[CHECK] Validando producto dentro del carrito...")
    assert "/cart.html" in driver.current_url, "No se redirigió a la página del carrito"
    
    nombre_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_en_carrito == nombre_prod, f"Error de integridad: {nombre_en_carrito} != {nombre_prod}"
    
    print(f"--- TEST FINALIZADO CON ÉXITO: {nombre_en_carrito} verificado ---")