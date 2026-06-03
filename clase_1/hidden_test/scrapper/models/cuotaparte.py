# models/cuotaparte.py

from dataclasses import dataclass

@dataclass
class Cuotaparte:

    fondo_id: str
    clase: str

    fecha: str

    numero_fondo: str
    nombre_fondo: str

    valor: float