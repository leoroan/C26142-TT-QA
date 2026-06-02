# Resolución - Clase 12: Ciclo de vida completo (E2E)

## 1. Crear el script de prueba (`tests_api/test_post_lifecycle.py`)
Crear el archivo dentro de tu carpeta `tests_api/`. Asegúrate de tener instalada la librería `faker` (puedo instalarla con `pip install faker` desde la terminal).

## 2. Actualizar pytest.ini
Para que el marker @pytest.mark.e2e que añadimos no arroje advertencias en la consola y cumpla con la "Definition of Done", debo agregarlo a mi archivo pytest.ini en la raíz del proyecto.
[pytest]
markers =
    smoke: pruebas críticas y rápidas
    exception: casos que validan manejo de errores
    api: pruebas de servicios de backend (API REST)
    e2e: pruebas end-to-end de flujos completos

## 3. Comandos para Ejecutar
Para correr esta prueba específica simulando el pipeline y ver la salida en consola, ejecutando:

pytest tests_api/test_post_lifecycle.py -m e2e -v -s

___

*respuesta  obtenida en mi caso de propyecto :*
- tests_api/test_post_lifecycle.py::test_post_lifecycle 
- [INFO] Recurso creado exitosamente con ID: 101
- [INFO] Título del recurso 101 actualizado mediante PATCH.
- [INFO] Recurso 101 eliminado exitosamente.
- [INFO] Flujo E2E completado en 1.53s.
- PASSED
