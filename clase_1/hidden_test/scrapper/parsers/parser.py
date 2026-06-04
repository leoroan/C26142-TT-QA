from bs4 import BeautifulSoup
from datetime import datetime

from models.fondo import Fondo

BASE_URL = "https://www.provinciafondos.com.ar"


def parse_fondos(html):
    soup = BeautifulSoup(html, "html.parser")

    fondos = []
    seen_ids = set()

    cards = soup.select("div.shadow-lg")

    for card in cards:

        try:

            link = card.select_one("a[href*='/nuestros-fondos/']")

            if not link:
                continue

            href = link.get("href", "").strip()

            fondo_id = href.split("/")[-1]

            if fondo_id in seen_ids:
                continue

            seen_ids.add(fondo_id)

            nombre = card.select_one("div.bg-primary-light span.font-bold").get_text(
                strip=True
            )

            rows = card.select("div.py-2.flex")

            moneda = None
            riesgo = None
            horizonte = None
            categoria = None
            variacion_diaria = None

            # fila 1
            if len(rows) >= 1:

                texto = rows[0].get_text(" ", strip=True)

                if "USD" in texto:
                    moneda = "USD"

                elif "Pesos" in texto:
                    moneda = "ARS"

                riesgo_el = rows[0].select_one("span.capitalize")

                if riesgo_el:
                    riesgo = riesgo_el.get_text(strip=True)

            # fila 2
            if len(rows) >= 2:

                spans = rows[1].select("span")

                if len(spans) >= 1:
                    horizonte = spans[0].get_text(" ", strip=True)

                if len(spans) >= 2:
                    categoria = spans[-1].get_text(strip=True)

            # fila 3
            if len(rows) >= 3:

                texto = rows[2].get_text(" ", strip=True)

                if "%" in texto:

                    valor = texto.split("%")[0].split()[-1].replace(",", ".")

                    variacion_diaria = float(valor)

            fondos.append(
                Fondo(
                    id=fondo_id,
                    nombre=nombre,
                    moneda=moneda,
                    riesgo=riesgo,
                    horizonte=horizonte,
                    categoria=categoria,
                    variacion_diaria=variacion_diaria,
                    url_detalle=f"{BASE_URL}{href}",
                    fecha_scraping=datetime.now().isoformat(),
                )
            )

        except Exception as e:

            print(f"Error parseando fondo: {e}")

    return fondos
