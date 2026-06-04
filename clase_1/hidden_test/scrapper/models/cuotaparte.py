# models/cuotaparte.py

from dataclasses import dataclass

@dataclass
class Cuotaparte:

    fondo_id: str
    nombre_fondo: str
    fecha: str
    clase: str
    numero_fondo: str
    valor: float


