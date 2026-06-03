from bs4 import BeautifulSoup

from models.cuotaparte import Cuotaparte


def parse_cuotapartes(html, fondo_id):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    resultados = []

    table = soup.select_one("table")

    if not table:
        return resultados

    rows = table.select("tbody tr")

    for row in rows:

        cols = row.select("td")

        if len(cols) < 4:
            continue

        fecha = cols[0].get_text(strip=True)

        numero_fondo = cols[1].get_text(strip=True)

        nombre_fondo = cols[2].get_text(strip=True)

        valor = cols[3].get_text(strip=True)

        resultados.append(
            Cuotaparte(
                fondo_id=fondo_id,
                clase="Clase A",
                fecha=fecha,
                numero_fondo=numero_fondo,
                nombre_fondo=nombre_fondo,
                valor=float(valor),
            )
        )

    return resultados