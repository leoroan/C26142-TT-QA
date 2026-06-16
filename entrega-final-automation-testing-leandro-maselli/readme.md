# Framework de Automatización de Pruebas

## 📌 Descripción

Proyecto es un framework de automatización de pruebas desarrollado en Python, que combina pruebas UI, API y BDD. 

Incluye ejecución automatizada, reportes HTML, logging y captura de evidencia en fallos.

---

## 🧪 Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- Requests
- Behave (BDD)
- Faker
- pytest-html

---

## 📂 Estructura del proyecto

  - pages/ # Page Object Model (UI)
  - tests/ # Tests UI con Pytest
  - tests_api/ # Tests de API con Requests
  - tests_behave/ # Integración Behave + Pytest
  - features/ # Features BDD (Gherkin)
  - datos/ # Datos CSV y JSON
  - utils/ # Logger y utilidades
  - logs/ # Logs de ejecución
  - reports/ # Reportes HTML y JSON

## ▶️ Instalación

```bash
pip install -r requirements.txt
```

▶️ Ejecución de pruebas
-----------------------

### Ejecutar todas las pruebas

```
pytest
```

* * * * *

### Ejecutar pruebas específicas

```
 - pytest tests/
 - pytest tests_api/
 - pytest tests_behave/
```

* * * * *

### Ejecutar BDD (Behave)

```
behave
```

📊 Reportes
-----------

Se generan automáticamente en:

```
reports/report.html
```

Incluyen:

-   resultados de tests
-   duración
-   fallos
-   evidencia visual

📸 Capturas de pantalla
-----------------------

Cuando un test falla, se genera automáticamente una captura en:

```
reports/screens/
```

* * * * *

🌐 API Testing
--------------

Se utilizan endpoints de JSONPlaceholder:

-   GET /posts
-   POST /posts
-   PATCH /posts
-   DELETE /posts

* * * * *

🧠 Buenas prácticas aplicadas
-----------------------------

-   Page Object Model
-   Data-driven testing (CSV/JSON)
-   Separación de capas
-   Logging centralizado
-   Hooks de Pytest
-   BDD con Gherkin

* * * * *

🚀 Autor
--------

Leandro Maselli, para Talento-Tech:Automatización QA 2026

