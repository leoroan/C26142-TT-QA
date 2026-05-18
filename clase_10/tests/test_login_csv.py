import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_login

# 1. Cargamos los datos con el CSV externo
CASOS_LOGIN = leer_csv_login('datos/login.csv')

# 2. Parametrizamos inyectando los datos en las variables del test
@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN)
def test_login_desde_csv(driver, usuario, clave, debe_funcionar, descripcion):
    """Test parametrizado que verifica el login con datos del CSV"""
    
    print(f"\n[INFO] Ejecutando escenario: {descripcion}")
    
    # Instanciamos la página y ejecutamos las acciones
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.completar_usuario(usuario)
    login_page.completar_clave(clave)
    login_page.hacer_clic_login()
    
    # 3. Lógica condicional: Validamos según lo que diga el CSV
    if debe_funcionar:
        assert "inventory.html" in driver.current_url, f"Falló el login para el usuario válido: {usuario}"
    else:
        assert "inventory.html" not in driver.current_url, f"Se permitió el ingreso al usuario inválido: {usuario}"


@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    """Test de smoke para verificar que al menos un login funciona rápido"""
    
    print("\n[INFO] Ejecutando Smoke Test de Login...")
    login_page = LoginPage(driver)
    
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    
    assert "inventory.html" in driver.current_url