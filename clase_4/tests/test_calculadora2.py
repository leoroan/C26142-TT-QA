from clase_4.calculadora import sumar, restar, multiplicar, dividir
import pytest

# =====================================================================
# 1. FIXTURES (@pytest.fixture)
# Preparan datos antes de los tests. Centralizan la configuración.
# =====================================================================
@pytest.fixture
def numeros_enteros():
    """Prepara dos enteros comunes para ser inyectados en las pruebas."""
    return 20, 5

@pytest.fixture
def numeros_decimales():
    """Prepara dos números con decimales (0.1, 0.2) para pruebas de precisión."""
    return 0.1, 0.2


# =====================================================================
# 2. PARAMETRIZACIÓN (@pytest.mark.parametrize) y MARKERS
# Evalúan una misma función con múltiples combinaciones de datos.
# =====================================================================
@pytest.mark.smoke
@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (2, 3, 5),        # Suma de positivos
        (-2, -3, -5),     # Suma de negativos
        (2.5, 0.5, 3.0),  # Suma con decimales
        (0, 0, 0)         # Suma con ceros
    ]
)
def test_sumar_varios(a, b, esperado):
    """Prueba parametrizada y marcada como 'smoke' para validar escenarios de suma."""
    print(f"\n[INFO] Suma parametrizada: {a} + {b} == {esperado}")
    assert sumar(a, b) == esperado

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (10, 5, 5),       # Resta de positivos
        (-1, -2, 1),      # Resta de negativos
        (3.5, 1.5, 2.0)   # Resta con decimales
    ]
)
def test_restar_varios(a, b, esperado):
    """Prueba parametrizada para validar múltiples escenarios de resta."""
    print(f"\n[INFO] Resta parametrizada: {a} - {b} == {esperado}")
    assert restar(a, b) == esperado


# =====================================================================
# 3. USO DE FIXTURES Y ASERCIONES AVANZADAS (pytest.approx)
# =====================================================================
def test_multiplicar_enteros(numeros_enteros):
    """Verifica la multiplicación utilizando el fixture de enteros."""
    a, b = numeros_enteros
    print(f"\n[INFO] Multiplicación con enteros: {a} * {b} == 100")
    assert multiplicar(a, b) == 100

def test_multiplicar_preciso(numeros_decimales):
    """Verifica multiplicación de flotantes manejando imprecisión con approx."""
    a, b = numeros_decimales
    print(f"\n[INFO] Multiplicación precisa (flotantes): {a} * {b}")
    # Se usa approx() porque 0.1 * 0.2 en Python suele dar 0.020000000000000004
    assert multiplicar(a, b) == pytest.approx(0.02) 

def test_dividir_enteros(numeros_enteros):
    """Verifica que la división de los enteros provistos por el fixture sea correcta."""
    a, b = numeros_enteros
    print(f"\n[INFO] División con fixture: {a} / {b} == 4")
    assert dividir(a, b) == 4


# =====================================================================
# 4. MANEJO DE EXCEPCIONES (@pytest.mark.exception)
# =====================================================================
@pytest.mark.exception
def test_dividir_por_cero():
    """Valida que se lance un ValueError al intentar dividir por cero."""
    print("\n[INFO] Ejecutando prueba de excepción (ValueError): 1 / 0")
    with pytest.raises(ValueError):
        dividir(1, 0)