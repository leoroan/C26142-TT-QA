from dataclasses import dataclass

@dataclass
class FactSheet:

    fondo_id: str

    fecha_reporte: str | None = None

    moneda: str | None = None
    riesgo: str | None = None
    horizonte_inversion: str | None = None
    perfil_inversor: str | None = None
    clasificacion: str | None = None

    patrimonio_neto: str | None = None
    valor_cuotaparte: str | None = None

    rendimiento_7_dias: str | None = None
    rendimiento_1_mes: str | None = None
    rendimiento_90_dias: str | None = None
    rendimiento_180_dias: str | None = None
    rendimiento_anual: str | None = None
    rendimiento_12_meses: str | None = None

    benchmark: str | None = None

    honorarios_sg_sd: str | None = None
    gastos_gestion: str | None = None
    honorarios_exito: str | None = None

    liquidez_pct: str | None = None
    plazo_fijo_pct: str | None = None
    caucion_pct: str | None = None