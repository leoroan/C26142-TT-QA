from dataclasses import dataclass
from typing import Optional


@dataclass
class Tenencia:

    fondo_id: str

    nombre: str

    porcentaje: Optional[float]

    fecha_scraping: str