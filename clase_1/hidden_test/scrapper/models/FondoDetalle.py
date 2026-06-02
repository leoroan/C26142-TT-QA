from dataclasses import dataclass
from typing import Optional


@dataclass
class FondoDetalle:
    fondo_id: str

    patrimonio: Optional[float]
    cuotaparte: Optional[float]
    benchmark: Optional[str]
    plazo_rescate: Optional[str]

    composicion: Optional[dict]

    honorarios: Optional[dict]

    reglamento_url: Optional[str]

    fecha_scraping: str