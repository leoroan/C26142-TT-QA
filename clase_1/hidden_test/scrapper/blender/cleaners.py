import pandas as pd

# Acá vive TODO el infierno de normalización.

def parse_decimal(
    value
):
    if pd.isna(value):
        return None

    value = str(value)

    value = (
        value
        .replace(".", "")
        .replace(",", ".")
        .replace("%", "")
        .strip()
    )

    try:
        return float(value)

    except:
        return None

def parse_date(
    series,
    fmt=None
):
    return pd.to_datetime(
        series,
        format=fmt,
        errors="coerce"
    )
    
def clean_fondos(df):

    df["variacion_diaria"] = pd.to_numeric(
        df["variacion_diaria"],
        errors="coerce"
    )

    df["fecha_scraping"] = parse_date(
        df["fecha_scraping"]
    )

    return df
  
def clean_cuotapartes(df):

    df["fecha"] = parse_date(
        df["fecha"],
        "%d/%m/%Y"
    )

    df["valor"] = (
        df["valor"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )

    df["valor"] = pd.to_numeric(
        df["valor"],
        errors="coerce"
    )

    return df
  
def clean_factsheets(df):

    numeric_columns = [
        "rendimiento_1_mes",
        "rendimiento_12_meses",
        "liquidez_pct",
        "plazo_fijo_pct",
        "caucion_pct",
    ]

    for col in numeric_columns:

        df[col] = df[col].apply(
            parse_decimal
        )

    df["fecha_reporte"] = parse_date(
        df["fecha_reporte"],
        "%d-%b-%y"
    )

    return df

def clean_detalles(df):

    numeric_columns = [
        "volatilidad_anual",
        "rendimiento_ytd",
        "rendimiento_mes",
        "patrimonio",
    ]

    for col in numeric_columns:

        df[col] = df[col].apply(
            parse_decimal
        )

    df["fecha_informacion"] = parse_date(
        df["fecha_informacion"]
    )

    df["fecha_scraping"] = parse_date(
        df["fecha_scraping"]
    )

    return df