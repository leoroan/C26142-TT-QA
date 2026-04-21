# Pre-entrega Automation Testing - [Leandro Maselli]

## Propósito
Automatización del flujo principal de compra en SauceDemo, incluyendo login, validación de catálogo y gestión de carrito de compras.

## Tecnologías Utilizadas
* **Python 3.x**
* **Selenium WebDriver 4**
* **Pytest** (Framework de pruebas)
* **Pytest-HTML** (Generación de reportes)
* **Webdriver-Manager** (Gestión automática de drivers)

## Instalación
1. Clonar el repositorio.
2. Instalar dependencias:
   ```bash
   pip install selenium webdriver-manager pytest pytest-html
   ```

## Ejecución de Pruebas

**Generar reporte en HTML de las pruebas realizadas:**
```bash
pytest pre-entrega/tests/test_saucedemo.py -v --html=pre-entrega/reports/reporte.html
```

**Generar reporte en CONSOLA de las pruebas realizadas:**
```bash
pytest pre-entrega/tests/test_saucedemo.py -v -s --html=pre-entrega/reports/reporte.html
```