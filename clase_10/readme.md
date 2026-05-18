# Ejecutar los tests

*asegurate de estar en la carpeta de la clase_10!! (...\C26142-TT-QA\clase_10> )*

- Ejecutar todos los tests
  ```bash
  pytest tests/ -v -s
  ```
- Ejecutar solo tests de login
  ```bash
  pytest tests/test_login_csv.py -v -s
  ```
- Ejecutar solo tests de carrito
  ```bash
  pytest tests/test_carrito_json.py -v -s
  ```
- Ejecutar tests de smoke
  ```bash
  pytest -m smoke -v -s
  ```
