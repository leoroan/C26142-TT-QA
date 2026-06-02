from pathlib import Path
from datetime import datetime

from fetcher import get_detail_html, get_html
from parser import parse_fondos
from storage import save_csv


BASE_DIR = Path(__file__).resolve().parent

SNAPSHOTS_DIR = BASE_DIR / "snapshots"

LIST_DIR = SNAPSHOTS_DIR / "list"
DETAIL_DIR = SNAPSHOTS_DIR / "detail"

LIST_DIR.mkdir(parents=True, exist_ok=True)
DETAIL_DIR.mkdir(parents=True, exist_ok=True)


def main():

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    html = get_html()

    fondos = parse_fondos(html)

    print(f"Fondos encontrados: {len(fondos)}")

    # guardar html listado

    list_html_file = (
        LIST_DIR /
        f"fondos_{timestamp}.html"
    )

    with open(
        list_html_file,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(html)

    # guardar csv

    csv_file = (
        LIST_DIR /
        f"fondos_{timestamp}.csv"
    )

    save_csv(fondos, csv_file)

    print(f"CSV generado: {csv_file}")

    # probar detalle con un fondo

    fondo = fondos[0]

    detail_html = get_detail_html(
        fondo.url_detalle
    )

    detail_file = (
        DETAIL_DIR /
        f"detalle_{fondo.id}_{timestamp}.html"
    )

    with open(
        detail_file,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(detail_html)

    print(
        f"Detalle generado: {detail_file}"
    )


if __name__ == "__main__":
    main()