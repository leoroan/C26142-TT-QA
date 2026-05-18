import csv
import json
import pathlib

def leer_csv_login(ruta_archivo):
    """
    Lee el archivo CSV de credenciales de login.
    Retorna lista de tuplas: (usuario, clave, debe_funcionar, descripcion)
    """
    datos = []
    ruta = pathlib.Path(ruta_archivo)
    
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Convertimos el texto 'True'/'False' del CSV a un booleano real de Python
            debe_funcionar = fila['debe_funcionar'].lower() == 'true'
            
            # Extraemos las 4 columnas de tu CSV
            datos.append((
                fila['usuario'], 
                fila['clave'], 
                debe_funcionar, 
                fila['descripcion']
            ))
    return datos

def leer_json_productos(ruta_archivo):
    """
    Lee el archivo JSON de productos.
    Retorna la lista completa de diccionarios.
    """
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        productos = json.load(archivo)
    return productos