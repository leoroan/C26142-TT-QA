# Clase N° 11: Automatización de Pruebas de API - Parte 1

_resumen de clase con ia_

## Resumen de Implementación de Pruebas de API con Pytest

Esta suite de pruebas automatizadas valida endpoints de una API REST utilizando Python, la librería `requests` para las peticiones HTTP y `pytest` como framework de testing.

### 1. Parametrización de Pruebas

* **`@pytest.mark.parametrize`:** Se utilizó para ejecutar una misma función de prueba múltiples veces inyectando diferentes conjuntos de datos. Esto optimiza el código y evita la repetición.
* **Cobertura de escenarios:** Se estructuraron tuplas y diccionarios para evaluar tanto **casos felices** (datos válidos, respuestas 200 y 201) como **casos negativos** (datos faltantes, respuestas 400).

### 2. Interacción con Métodos HTTP

* **GET (`requests.get`):** Implementado para consultar recursos (lista de usuarios), validando que la API devuelva la información solicitada correctamente.
* **POST (`requests.post`):** Implementado para el envío de payloads en formato JSON (creación de usuarios y login), comprobando que el servidor procese las entradas y genere nuevos registros o tokens.

### 3. Validaciones Avanzadas (Asserts)

* **Códigos de Estado:** Verificación estricta de los *Status Codes* devueltos por el servidor (200, 201, 400) según la acción realizada.
* **Lógica de Conjuntos (Sets):** Uso de `set(usuario.keys())` para comparar las claves de un diccionario. Es una forma *Pythonic* y altamente eficiente de validar que un JSON contenga toda la estructura requerida.
* **Validaciones Dinámicas:** Uso del módulo `datetime` para verificar que la fecha de creación (`createdAt`) coincida con el año actual, logrando un test que no caduca con el tiempo.
* **Validación de Formatos:** Uso del método de string `.endswith('.jpg')` para asegurar que los enlaces a los avatares tengan la extensión correcta.

### 4. Configuración y Modularización

* **Marcadores Custom (`@pytest.mark.api`):** Etiquetado estratégico de las funciones para categorizarlas. Esto permite ejecutar comandos específicos en la terminal para correr únicamente las pruebas de backend, aislándolas de las pruebas de UI.
* **Archivo `pytest.ini`:** Registro de los marcadores personalizados en la raíz del proyecto para estandarizar la configuración del entorno de pruebas y evitar advertencias en consola.


Comandos de ejecución esperados:

Ejecutar solo tests de API

                  pytest -m api -v

Ejecutar todo (UI + API)

                 pytest tests/ tests_api/ -v

Generar reporte combinado

          pytest tests/ tests_api/ --html=reporte_completo.html