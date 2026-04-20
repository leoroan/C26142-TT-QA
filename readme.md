
# Proyecto de Automatización de Testing

## Estructura del Proyecto

- [Clase 1](https://github.com/leoroan/C26142-TT-QA/tree/main/clase_1)
- [Clase 2](https://github.com/leoroan/C26142-TT-QA/tree/main/clase_2)
- [Clase 3](https://github.com/leoroan/C26142-TT-QA/tree/main/clase_3)
- [Clase 4](https://github.com/leoroan/C26142-TT-QA/tree/main/clase_4)
- [Clase 5](https://github.com/leoroan/C26142-TT-QA/tree/main/clase_5)
- [Clase 6](https://github.com/leoroan/C26142-TT-QA/tree/main/clase_6)
- [Clase 7](https://github.com/leoroan/C26142-TT-QA/tree/main/clase_7)
- [Clase 8](https://github.com/leoroan/C26142-TT-QA/tree/main/clase_8)
- [Pre-entrega](https://github.com/leoroan/C26142-TT-QA/tree/main/pre-entrega)


## Descripción

Este repositorio contiene recursos y ejemplos para el curso de automatización de testing.

## Cómo usar

### Ejecutar tests con pytest

Para ejecutar los tests, utiliza los siguientes comandos:

```bash
pytest -v .\test_someDesireScript.py --html=report.html --self-contained-html

- Muestra cómo filtrar la ejecución:

pytest -m smoke # solo tests “sumar”

pytest -m exception # solo tests “dividir” con error

- Reporte HTML

Genera el informe con: pytest --html=report.html. (o el otro de arriba)

```
**Ejemplo de reporte generado**
- [Reporte Calculadora.py con pytest](https://github.com/leoroan/C26142-TT-QA/blob/main/clase_4/tests/report.html) 

Este comando ejecutará los tests en modo verbose (`-v`), generará un reporte HTML autónomo que se puede abrir en cualquier navegador.

## Módulos Disponibles

- **Clase 1**: Inicializacion, extensiones y brebe test.py file.
- **Clase 2**: dos actividades simples para verificar el entorno.
- **Clase 3**: un script de una calculadora con validaciones de errores con try/except
- **Clase 4**: Introduccion a PyTest y Automatizacion Básica (proeycto con practica)
- **Clase 5**: Introducción a HTML y Estructura de Páginas Web
- **Clase 6**: DOM para Automatización
- **Clase 7**: Introducción a Selenium WebDriver
- **Clase 8**: Localización de Elementos y Acciones en Selenium
- **pre entrega**: PRE-ENTREGA | Automatización QA


## Requisitos

- Python 3.14+
- pytest
- selenium
- Dependencias listadas en `requirements.txt` (not-yet)

## Instalación

```bash
pip install -r requirements.txt
```

## Selenium WebDrivers 
*Cada navegador necesita su propio "conductor" para que Selenium pueda controlarlo:*

| Navegador | Driver | Descarga |
| --- | --- | --- |
| Chrome | ChromeDriver | https://googlechromelabs.github.io/chrome-for-testing/ |
| Firefox | GeckoDriver | https://github.com/mozilla/geckodriver/releases |
| Edge | msedgedriver | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |

### Importante: Compatibilidad de versiones

**La versión del driver debe coincidir con la de tu navegador.** 

Por ejemplo, si tienes Chrome 123, descarga ChromeDriver 123. Si las versiones no coinciden obtendrás errores como `SessionNotCreatedException`.

#### Ejemplo en windows x64

Ver versión de ChromeDriver
Si ya descargaste el chromedriver.exe:

1. Abrí la terminal en VS Code con Ctrl + ñ
2. Andá a la carpeta donde tenés el driver
3. Ejecutá: .\chromedriver.exe --version

tambien podes descargar el driver dsde el enlace
4. lo ejecutas y dejas correindo en el backl (funciona solo local)
5. listo

**Tip**: Desde Selenium 4.6+ podés usar `Selenium Manager` y evitar manejar drivers manualmente. Solo haces `webdriver.Chrome()` y descarga el driver correcto automáticamente.