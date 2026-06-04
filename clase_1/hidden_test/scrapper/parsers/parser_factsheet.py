import re

from models.factsheet import FactSheet


def find_value(text, label):

    pattern = rf"{re.escape(label)}\s*:?\s*(.+)"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return None


def extract_rendimiento(lines, periodo):

    for line in lines:

        pattern = rf"{re.escape(periodo)}" rf"\s+([0-9.,]+%)"

        match = re.search(pattern, line, re.IGNORECASE)

        if match:
            return match.group(1)

    return None


def extract_percentage_after(text, label):

    for index, line in enumerate(text):

        if label.lower() in line.lower():

            # porcentaje en la misma línea
            match = re.search(r"([0-9.,]+%)", line)

            if match:
                return match.group(1)

            # porcentaje en línea siguiente
            if index + 1 < len(text):

                next_line = text[index + 1]

                match = re.search(r"([0-9.,]+%)", next_line)

                if match:
                    return match.group(1)

    return None


def extract_section(text, start, end=None):

    if end:

        pattern = rf"{re.escape(start)}" rf"(.*?)" rf"{re.escape(end)}"

    else:

        pattern = rf"{re.escape(start)}" rf"(.*)"

    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)

    if not match:
        return ""

    return match.group(1).strip()


def parse_factsheet(text, fondo_id, fondo_nombre):

    info_section = extract_section(
        text, "INFORMACIÓN DEL FCI", "COMPOSICIÓN DE LA CARTERA"
    )

    rendimiento_section = extract_section(
        text, "RENDIMIENTO HISTÓRICO", "COMPOSICIÓN DE LA CARTERA"
    )

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    factsheet = FactSheet(fondo_id=fondo_id, fondo_nombre=fondo_nombre)

    factsheet.rendimiento_7_dias = extract_rendimiento(lines, "7 días")

    factsheet.rendimiento_1_mes = extract_rendimiento(lines, "1 mes")

    factsheet.rendimiento_90_dias = extract_rendimiento(lines, "90 días")

    factsheet.rendimiento_180_dias = extract_rendimiento(lines, "180 días")

    factsheet.rendimiento_anual = extract_rendimiento(lines, "En el año")

    factsheet.rendimiento_12_meses = extract_rendimiento(lines, "12 meses")

    factsheet.fecha_reporte = find_value(text, "Fecha Reporte")

    factsheet.moneda = find_value(text, "Moneda del FCI")

    factsheet.riesgo = find_value(text, "Riesgo")

    factsheet.horizonte_inversion = find_value(text, "Horizonte de inversión")

    factsheet.perfil_inversor = find_value(text, "Perfil inversor")

    factsheet.clasificacion = find_value(text, "Clasificación")

    factsheet.patrimonio_neto = find_value(text, "Patrimonio neto")

    factsheet.valor_cuotaparte = find_value(text, "Valor Cuotaparte")

    factsheet.benchmark = find_value(text, "Benchmark")

    factsheet.honorarios_sg_sd = extract_percentage_after(lines, "Honorarios SG + SD")

    factsheet.gastos_gestion = extract_percentage_after(lines, "Gastos de gestión")

    factsheet.honorarios_exito = extract_percentage_after(lines, "Honorarios de éxito")

    factsheet.liquidez_pct = extract_percentage_after(lines, "Liquidez")

    factsheet.plazo_fijo_pct = extract_percentage_after(lines, "Plazo Fijo")

    factsheet.caucion_pct = extract_percentage_after(lines, "Caución")

    return factsheet
