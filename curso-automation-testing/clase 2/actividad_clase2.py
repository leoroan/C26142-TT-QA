# Actividad 1: Solicitar datos del usuario e imprimir mensaje personalizado
print("=== Actividad 1 ===")
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")
profesion = input("¿Cuál es tu profesión? ")

print(f"\n¡Hola {nombre}! Tienes {edad} años y trabajas como {profesion}.")

# Actividad 2: Mostrar los primeros 10 números pares
print("\n=== Actividad 2 ===")
print("Los primeros 10 números pares son:")

contador = 0
numero = 1

while contador < 10:
  if numero % 2 == 0:
    print(numero, end=" ")
    contador += 1
  numero += 1

print()