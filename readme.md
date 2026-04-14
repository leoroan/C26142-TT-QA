
# Proyecto de Automatización de Testing

## Estructura del Proyecto

- [Clase 1](https://github.com/leoroan/C26142-TT-QA/tree/main/clase_1)
- [Clase 2](https://github.com/leoroan/C26142-TT-QA/tree/main/clase_2)
- [Clase 3](https://github.com/leoroan/C26142-TT-QA/tree/main/clase_3)
- [Clase 4](https://github.com/leoroan/C26142-TT-QA/tree/main/clase_4)


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
- **Clase 4**: Intrudccion a PyTest y Automatizacion Básica (proeycto con practica)

## Requisitos

- Python 3.14+
- pytest
- Dependencias listadas en `requirements.txt` (not-yet)

## Instalación

```bash
pip install -r requirements.txt
```



