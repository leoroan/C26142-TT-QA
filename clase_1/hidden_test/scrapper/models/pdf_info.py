from dataclasses import dataclass
from decimal import Decimal
from datetime import date


@dataclass
class PdfInfo:

    fondo_id: str

    fecha_reporte: date | None

    patrimonio: Decimal | None

    benchmark: str | None

    clasificacion: str | None

    riesgo: str | None

    rendimiento_7_dias: float | None

    rendimiento_1_mes: float | None

    rendimiento_90_dias: float | None

    rendimiento_180_dias: float | None

    rendimiento_anual: float | None