from dataclasses import dataclass
from typing import Optional

@dataclass
class Fondo:
    id: str
    nombre: str
    moneda: Optional[str]
    riesgo: Optional[str]
    horizonte: Optional[str]
    categoria: Optional[str]
    variacion_diaria: Optional[float]
    url_detalle: str
    fecha_scraping: str