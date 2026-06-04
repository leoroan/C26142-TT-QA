import re

from utils import parse_percentage, parse_money, parse_spanish_date
from bs4 import BeautifulSoup
from datetime import datetime

from models.fondo_detalle import FondoDetalle
from models.tenencia import Tenencia


def parse_fondo_detalle(html, fondo_id):

    soup = BeautifulSoup(html, "html.parser")

    descripcion = None

    volatilidad_anual = None
    rendimiento_ytd = None
    rendimiento_mes = None
    duration = None

    fecha_informacion = None
    patrimonio = None

    factsheet_url = None
    reglamento_url = None
    calificaciones_url = None

    # descripción

    descripcion_el = soup.select_one("h1 + p")

    if descripcion_el:
        descripcion = descripcion_el.get_text(" ", strip=True)

    # rendimiento

    rendimiento_card = None

    cards = soup.select("div.shadow-\\[5px_5px_44px_0px_rgba\\(0\\,0\\,0\\,0\\.1\\)\\]")

    for card in cards:

        title = card.select_one("h3")

        if not title:
            continue

        text = title.get_text(strip=True)

        if text == "Rendimiento":
            rendimiento_card = card
            break

    if rendimiento_card:

        rows = rendimiento_card.select("div.flex.justify-between")

        for row in rows:

            spans = row.select("span")

            if len(spans) < 2:
                continue

            label = spans[0].get_text(" ", strip=True)

            value = spans[1].get_text(" ", strip=True)

            if "Volatilidad" in label:
                volatilidad_anual = parse_percentage(value)

            elif "YTD" in label:
                rendimiento_ytd = parse_percentage(value)

            elif "mes" in label:
                rendimiento_mes = parse_percentage(value)

            elif "Duration" in label:
                duration = value

    # información

    info_card = None

    for card in cards:

        title = card.select_one("h3")

        if not title:
            continue

        text = title.get_text(strip=True)

        if text == "Información":
            info_card = card
            break

    if info_card:

        info_text = info_card.get_text(" ", strip=True)

        fecha_match = re.search(
            r"Información al (\d{1,2} de \w+ de \d{4})", info_text, re.IGNORECASE
        )

        if fecha_match:

            fecha_informacion = parse_spanish_date(fecha_match.group(1))

        patrimonio_match = re.search(
            r"Patrimonio del Fondo \$ ([\d\.\,]+)",
            info_text,
        )

        if patrimonio_match:

            patrimonio = parse_money(patrimonio_match.group(1))

        links = info_card.select("a[href]")

        for link in links:

            href = link.get("href", "")

            label = link.get_text(" ", strip=True)

            if "Fact" in label:
                factsheet_url = href

    # -------------------------
    # tenencias
    # -------------------------

    tenencias = []

    tenencias_title = soup.find("h3", string=lambda s: s and "Tenencias" in s)

    if tenencias_title:

        tenencias_card = tenencias_title.find_parent("div")

        rows = tenencias_card.select("div.flex.mb-8")

        for row in rows:

            spans = row.select("span")

            if len(spans) < 2:
                continue

            nombre = spans[0].get_text(" ", strip=True)

            porcentaje_text = spans[1].get_text(" ", strip=True)

            porcentaje = parse_percentage(porcentaje_text)

            tenencia = Tenencia(
                fondo_id=fondo_id,
                nombre=nombre,
                porcentaje=porcentaje,
                fecha_scraping=datetime.now().isoformat(),
            )

            tenencias.append(tenencia)

    detalle = FondoDetalle(
        fondo_id=fondo_id,
        descripcion=descripcion,
        volatilidad_anual=volatilidad_anual,
        rendimiento_ytd=rendimiento_ytd,
        rendimiento_mes=rendimiento_mes,
        duration=duration,
        fecha_informacion=fecha_informacion,
        patrimonio=patrimonio,
        factsheet_url=factsheet_url,
        fecha_scraping=datetime.now().isoformat(),
    )

    return detalle, tenencias
