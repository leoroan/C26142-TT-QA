from dataclasses import dataclass
from typing import Optional
from decimal import Decimal
from datetime import date

@dataclass
class FondoDetalle:

    fondo_id: str

    descripcion: Optional[str]

    volatilidad_anual: Optional[float]
    rendimiento_ytd: Optional[float]
    rendimiento_mes: Optional[float]

    duration: Optional[str]

    patrimonio: Optional[Decimal]

    fecha_informacion: Optional[date]

    factsheet_url: Optional[str]

    fecha_scraping: str