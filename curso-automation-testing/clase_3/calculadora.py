def sumar(a, b):
  """Suma dos números"""
  return a + b


def restar(a, b):
  """Resta dos números"""
  return a - b


def multiplicar(a, b):
  """Multiplica dos números"""
  return a * b


def dividir(a, b):
  """Divide dos números"""
  if b == 0:
    raise ValueError("División por cero")
  return a / b


def obtener_numeros():
  """Obtiene dos números del usuario"""
  while True:
    try:
      num1 = float(input("Ingresa el primer número: "))
      num2 = float(input("Ingresa el segundo número: "))
      return num1, num2
    except ValueError:
      print("Error: Debes ingresar números válidos (enteros o decimales)")


def obtener_operacion():
  """Obtiene la operación deseada"""
  operaciones_validas = ["1", "2", "3", "4"]
  while True:
    print("\n--- Calculadora ---")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    operacion = input("Elige una operación (1-4): ").strip()
    
    if operacion in operaciones_validas:
      return operacion
    print("Error: Debes ingresar una opción válida (1-4)")


def ejecutar_operacion(num1, num2, operacion):
  """Ejecuta la operación seleccionada"""
  operaciones = {
    "1": sumar,
    "2": restar,
    "3": multiplicar,
    "4": dividir
  }
  return operaciones[operacion](num1, num2)


def principal():
  """Función principal"""
  while True:
    try:
      operacion = obtener_operacion()
      num1, num2 = obtener_numeros()
      resultado = ejecutar_operacion(num1, num2, operacion)
      print(f"\nResultado: {resultado}\n")
    except ValueError as e:
      print(f"Error: {e}\n")
    except Exception as e:
      print(f"Error inesperado: {e}\n")
    
    while True:
      continuar = input("¿Deseas hacer otra operación? (s/n): ").lower().strip()
      if continuar in ["s", "n"]:
        break
      print("Por favor, ingresa 's' o 'n'")
    
    if continuar != "s":
      print("¡Hasta luego!")
      break


if __name__ == "__main__":
  principal()