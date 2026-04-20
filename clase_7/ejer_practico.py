from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Configuración de espera implícita (5 segundos)
driver.implicitly_wait(5)

try:
    # Paso 1: Navegación inicial
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()

    # Paso 2: Autenticación
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Paso 3: Ejecución del Login
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    # Paso 4: Validación de Redirección (URL)
    assert "/inventory.html" in driver.current_url, "Error: No se redirigió a la página de inventario."

    # Paso 5: Validación inmediata del título de la sección (Products)
    # Se coloca aquí para confirmar que la interfaz cargó correctamente tras el login
    titulo_seccion = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text
    assert titulo_seccion == "Products", f"Error: Título incorrecto: {titulo_seccion}"

    # Paso 6: Comprobación de existencia de productos en el DOM
    # Buscamos todos los elementos con la clase 'inventory_item'
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    
    # Confirmamos que la lista no esté vacía (aparece al menos un div.inventory_item)
    assert len(productos) > 0, "Error: El listado de productos está vacío."
    
    # Extraemos y mostramos en consola el nombre y precio del primer producto encontrado
    primer_nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"--- Datos del Inventario ---")
    print(f"Producto detectado: {primer_nombre} | Precio: {primer_precio}")

    # Paso 7: Interacción - Añadir primer producto al carrito
    productos[0].find_element(By.XPATH, ".//button[contains(@id,'add-to-cart')]").click()

    # Paso 8: Comprobación visual/consola de la cantidad en el carrito
    # Verificamos que el badge del carrito se actualice a '1'
    badge_texto = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge_texto == "1", f"Error: Se esperaba 1 item, pero hay {badge_texto}"
    print(f"Comprobación de cantidad: {badge_texto} producto(s) en el icono del carrito.")

    # Paso 9: Verificación de contenido en la página del carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    item_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    
    # Validamos que el nombre del producto en el carrito sea el mismo que seleccionamos
    assert item_en_carrito == primer_nombre, "Error: El producto en el carrito no es el esperado."
    print(f"Comprobación de nombre: El producto '{item_en_carrito}' se encuentra en el carrito correctamente.")

    # Paso 10: Finalización exitosa
    print("--- Resultado Final ---")
    print("Test OK")

except Exception as e:
    # Captura de cualquier interrupción o fallo de aserción
    print(f"FALLO DEL TEST: {e}")

finally:
    # Cierre preventivo del navegador para liberar memoria
    driver.quit()
    # Aseguramos el cierre de la sesión para evitar procesos zombis
    driver.quit()