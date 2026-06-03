import re

from decimal import Decimal
from datetime import datetime


def parse_percentage(value):

    if not value:
        return None

    value = (
        value
        .replace("%", "")
        .replace(",", ".")
        .strip()
    )

    try:
        return float(value)

    except:
        return None


def parse_money(value):

    if not value:
        return None

    cleaned = (
        value
        .replace("$", "")
        .replace(".", "")
        .replace(",", ".")
        .strip()
    )

    try:
        return Decimal(cleaned)

    except:
        return None


def parse_spanish_date(value):

    meses = {
        "enero": 1,
        "febrero": 2,
        "marzo": 3,
        "abril": 4,
        "mayo": 5,
        "junio": 6,
        "julio": 7,
        "agosto": 8,
        "septiembre": 9,
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12,
    }

    try:

        parts = value.lower().split()

        day = int(parts[0])

        month = meses[parts[2]]

        year = int(parts[4])

        return datetime(
            year,
            month,
            day
        ).date()

    except:
        return None
    
    
    import re
import unicodedata


def slugify(value):

    value = unicodedata.normalize(
        "NFKD",
        value
    ).encode(
        "ascii",
        "ignore"
    ).decode(
        "ascii"
    )

    value = value.lower()

    value = re.sub(
        r"[^a-z0-9]+",
        "_",
        value
    )

    value = value.strip("_")

    return value