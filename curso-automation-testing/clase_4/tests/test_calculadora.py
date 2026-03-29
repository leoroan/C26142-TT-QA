# from calculadora import sumar, restar, multiplicar, dividir # Asumiendo que las funciones vienen de aquí
# import pytest

# # =====================================================================
# # 1. FIXTURES (@pytest.fixture)
# # Un fixture prepara datos reutilizables antes del test para 
# # evitar código duplicado.
# # =====================================================================
# @pytest.fixture
# def numeros_enteros():
#     """Prepara dos enteros comunes para ser inyectados en las pruebas."""
#     return 20, 5

# # Nuevo test que utiliza el fixture inyectándolo como parámetro
# def test_dividir_enteros(numeros_enteros):
#     a, b = numeros_enteros
#     assert dividir(a, b) == 4


# # =====================================================================
# # 2. MARKERS (@pytest.mark.<etiqueta>)
# # Sirven para etiquetar los tests y poder filtrarlos o agruparlos 
# # al ejecutarlos desde la consola (ej: pytest -m smoke).
# # =====================================================================

# # Etiquetamos las sumas como pruebas críticas/rápidas usando 'smoke'
# @pytest.mark.smoke
# def test_sumar_positivo():
#     assert sumar(2, 3) == 5
    
# @pytest.mark.smoke
# def test_sumar_negativo():
#     assert sumar(-2, -3) == -5
    
# def test_restar_positivo():
#     assert restar(5, 2) == 3

# def test_multiplicar_positivo():
#     assert multiplicar(2, 3) == 6

# # Etiquetamos este test con 'exception' ya que valida un manejo de error
# @pytest.mark.exception
# def test_dividir_por_cero():
#     with pytest.raises(ValueError):
#         dividir(1, 0)


# # =====================================================================
# # 3. PARAMETRIZACIÓN (@pytest.mark.parametrize)
# # En lugar de tener funciones separadas para sumar_positivo y sumar_negativo,
# # este decorador permite probar múltiples combinaciones de datos en un solo test,
# # creando sub-tests por cada fila y aumentando la cobertura sin repetir código.
# # =====================================================================
# @pytest.mark.parametrize(
#     "a,b,esperado",
#     [
#         (1, 2, 3),        # Equivalente a sumar positivos
#         (-1, -1, -2),     # Equivalente a sumar negativos
#         (2.5, 0.5, 3),    # Suma con decimales
#         (0, 0, 0)         # Suma con ceros
#     ]
# )
# def test_sumar_varios(a, b, esperado):
#     assert sumar(a, b) == esperado



from calculadora import sumar, restar, multiplicar, dividir # Asumiendo que las funciones vienen de aquí
import pytest

# =====================================================================
# 1. FIXTURES (@pytest.fixture)
# Un fixture prepara datos reutilizables antes del test para 
# evitar código duplicado.
# =====================================================================
@pytest.fixture
def numeros_enteros():
    """Prepara dos enteros comunes para ser inyectados en las pruebas."""
    return 20, 5

# Nuevo test que utiliza el fixture inyectándolo como parámetro
def test_dividir_enteros(numeros_enteros):
    """Verifica que la división de los enteros provistos por el fixture sea correcta."""
    a, b = numeros_enteros
    print(f"\n[INFO] Ejecutando prueba de división con fixture: {a} / {b}")
    assert dividir(a, b) == 4


# =====================================================================
# 2. MARKERS (@pytest.mark.<etiqueta>)
# Sirven para etiquetar los tests y poder filtrarlos o agruparlos 
# al ejecutarlos desde la consola (ej: pytest -m smoke).
# =====================================================================

# Etiquetamos las sumas como pruebas críticas/rápidas usando 'smoke'
@pytest.mark.smoke
def test_sumar_positivo():
    """Verifica la suma de dos números positivos."""
    print("\n[INFO] Ejecutando prueba de suma: 2 + 3. Resultado esperado: 5")
    assert sumar(2, 3) == 5
    
@pytest.mark.smoke
def test_sumar_negativo():
    """Verifica la suma de dos números negativos."""
    print("\n[INFO] Ejecutando prueba de suma: -2 + (-3). Resultado esperado: -5")
    assert sumar(-2, -3) == -5
    
def test_restar_positivo():
    """Verifica la resta de dos números positivos."""
    print("\n[INFO] Ejecutando prueba de resta: 5 - 2. Resultado esperado: 3")
    assert restar(5, 2) == 3

def test_multiplicar_positivo():
    """Verifica la multiplicación de dos números positivos."""
    print("\n[INFO] Ejecutando prueba de multiplicación: 2 * 3. Resultado esperado: 6")
    assert multiplicar(2, 3) == 6

# Etiquetamos este test con 'exception' ya que valida un manejo de error
@pytest.mark.exception
def test_dividir_por_cero():
    """Valida que se lance un ValueError al intentar dividir por cero."""
    print("\n[INFO] Ejecutando prueba de excepción: 1 / 0. Resultado esperado: Error ValueError")
    with pytest.raises(ValueError):
        dividir(1, 0)


# =====================================================================
# 3. PARAMETRIZACIÓN (@pytest.mark.parametrize)
# En lugar de tener funciones separadas para sumar_positivo y sumar_negativo,
# este decorador permite probar múltiples combinaciones de datos en un solo test,
# creando sub-tests por cada fila y aumentando la cobertura sin repetir código.
# =====================================================================
@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (1, 2, 3),        # Equivalente a sumar positivos
        (-1, -1, -2),     # Equivalente a sumar negativos
        (2.5, 0.5, 3),    # Suma con decimales
        (0, 0, 0)         # Suma con ceros
    ]
)
def test_sumar_varios(a, b, esperado):
    """Prueba parametrizada para validar múltiples escenarios de suma de forma dinámica."""
    print(f"\n[INFO] Ejecutando suma parametrizada: {a} + {b}. Resultado esperado: {esperado}")
    assert sumar(a, b) == esperado