import pytest
import pathlib

# Carpeta donde guardaremos las capturas
target = pathlib.Path('reports/screens')
target.mkdir(parents=True, exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Se ejecuta después de cada fase de cada test. Captura pantalla si falla."""
    outcome = yield
    report = outcome.get_result()
    
    # Solo capturamos en fallos de la fase principal ('call')
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            file_name = target / f"{item.name}.png"
            driver.save_screenshot(str(file_name))
            
            # Adjuntamos la imagen al reporte HTML
            if hasattr(report, 'extra'):
                report.extra.append({
                    'name': 'screenshot',
                    'format': 'image',
                    'content': str(file_name)
                })