from datetime import datetime

from config import (
    SAVE_DEBUG_HTML,
    SAVE_FACTSHEET_TXT,
    PROCESS_ONLY_FIRST,
)

from paths import (
    ensure_directories,
    LIST_DIR,
    DETAIL_DIR,
    PDF_DIR,
    CUOTAPARTE_DIR,
)

from services.fondos_service import (
    obtener_fondos,
)

from services.detalle_service import (
    obtener_detalle,
)

from services.factsheet_service import (
    procesar_factsheet,
)

from services.cuotaparte_service import (
    obtener_cuotapartes,
)

from storage import (
    save_csv,
    save_detail_csv,
    save_cuotapartes_csv,
    save_factsheets_csv,
)

from utils import slugify


def save_text_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def process_factsheet(fondo, detalle, timestamp, factsheets):
    pdf_url = detalle.factsheet_url

    if not pdf_url:
        return

    safe_name = slugify(fondo.nombre)

    pdf_file = PDF_DIR / f"{safe_name}_factsheet_{timestamp}.pdf"

    txt_file = PDF_DIR / f"{safe_name}_factsheet_{timestamp}.txt"

    factsheet = procesar_factsheet(
        pdf_url,
        pdf_file,
        txt_file,
        fondo.id,
        fondo.nombre
    )

    print(f"Factsheet procesado: " f"{fondo.nombre}")

    factsheets.append(factsheet)


def process_cuotapartes(fondo, timestamp):
    safe_name = slugify(fondo.nombre)

    html, cuotapartes = obtener_cuotapartes(fondo)

    print(f"Cuotapartes encontradas: " f"{len(cuotapartes)}")

    if SAVE_DEBUG_HTML:

        html_file = CUOTAPARTE_DIR / f"{safe_name}_cuotapartes_{timestamp}.html"

        save_text_file(html_file, html)

    csv_file = CUOTAPARTE_DIR / f"{safe_name}_cuotapartes_{timestamp}.csv"

    save_cuotapartes_csv(cuotapartes, csv_file)

    print(f"CSV cuotapartes generado: " f"{csv_file}")


def process_fondo(fondo, timestamp, detalles, factsheets):
    print(f"\nProcesando detalle: " f"{fondo.nombre}")

    safe_name = slugify(fondo.nombre)

    detail_html, detalle, tenencias = obtener_detalle(fondo)

    detalles.append(detalle)

    if SAVE_DEBUG_HTML:

        detail_file = DETAIL_DIR / f"detalle_{safe_name}_{timestamp}.html"

        save_text_file(detail_file, detail_html)

    try:
        process_factsheet(fondo, detalle, timestamp, factsheets)

    except Exception as e:

        print(f"Error factsheet: {e}")

    try:
        process_cuotapartes(fondo, timestamp)

    except Exception as e:

        print(f"Error cuotapartes: {e}")


def main():
    ensure_directories()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    html, fondos = obtener_fondos()

    print(f"Fondos encontrados: " f"{len(fondos)}")

    csv_file = LIST_DIR / f"los_fondos_{timestamp}.csv"

    save_csv(fondos, csv_file)

    detalles = []
    factsheets = []

    fondos_to_process = fondos if PROCESS_ONLY_FIRST else fondos

    for fondo in fondos_to_process:

        try:

            process_fondo(fondo, timestamp, detalles, factsheets)

        except Exception as e:

            print(f"Error procesando " f"{fondo.nombre}: {e}")

    if detalles:

        detail_csv = DETAIL_DIR / f"detalles_{timestamp}.csv"

        save_detail_csv(detalles, detail_csv)

    if factsheets:

        factsheet_csv = PDF_DIR / f"factsheets_{timestamp}.csv"

        save_factsheets_csv(factsheets, factsheet_csv)


if __name__ == "__main__":
    main()
