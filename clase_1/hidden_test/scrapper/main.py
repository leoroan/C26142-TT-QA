from pathlib import Path
from datetime import datetime

from fetcher import (
    get_html,
    get_detail_html,
    download_pdf,
    get_cuotapartes_html,
)

from parsers.parser import (
    parse_fondos,
)

from parsers.parser_detalle import (
    parse_fondo_detalle,
)

from parsers.parser_pdf import (
    extract_pdf_text,
)

from parsers.parser_cuotaparte import (
    parse_cuotapartes,
)

from parsers.parser_factsheet import (
    parse_factsheet,
)

from storage import (
    save_csv,
    save_detail_csv,
    save_cuotapartes_csv,
    save_factsheets_csv,
)

from utils import slugify

SAVE_DEBUG_HTML = False
SAVE_FACTSHEET_TXT = True

BASE_DIR = Path(__file__).resolve().parent

SNAPSHOTS_DIR = BASE_DIR / "snapshots"

LIST_DIR = SNAPSHOTS_DIR / "list"
DETAIL_DIR = SNAPSHOTS_DIR / "detail"
PDF_DIR = SNAPSHOTS_DIR / "pdf"
CUOTAPARTE_DIR = SNAPSHOTS_DIR / "cuotapartes"

LIST_DIR.mkdir(
    parents=True,
    exist_ok=True
)

DETAIL_DIR.mkdir(
    parents=True,
    exist_ok=True
)

PDF_DIR.mkdir(
    parents=True,
    exist_ok=True
)

CUOTAPARTE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def main():

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    # -------------------------
    # listado principal
    # -------------------------

    html = get_html()

    fondos = parse_fondos(html)

    print(
        f"Fondos encontrados: "
        f"{len(fondos)}"
    )

    # guardar html listado para debug de html
    if SAVE_DEBUG_HTML:
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

        print(
            f"HTML listado generado: "
            f"{list_html_file}"
        )

    # guardar csv listado
    csv_file = (
        LIST_DIR /
        f"los_fondos_{timestamp}.csv"
    )

    save_csv(
        fondos,
        csv_file
    )

    print(
        f"CSV del listado de los fondos generado: "
        f"{csv_file}"
    )

    # -------------------------
    # detalles & factsheets
    # -------------------------

    detalles = []
    factsheets = [] 

    for fondo in fondos[:1]:

        print(
            f"\nProcesando detalle: "
            f"{fondo.nombre}"
        )

        try:

            safe_name = slugify(
                fondo.nombre
            )

            # -------------------------
            # detalle html
            # -------------------------

            detail_html = get_detail_html(
                fondo.url_detalle
            )

            if SAVE_DEBUG_HTML:
                detail_file = (
                    DETAIL_DIR /
                    f"detalle_{safe_name}_{timestamp}.html"
                )

                with open(
                    detail_file,
                    "w",
                    encoding="utf-8"
                ) as f:
                    f.write(detail_html)

                print(
                    f"HTML detalle del fondo, para DEBUG generado: "
                    f"{detail_file}"
                )

            # -------------------------
            # parse detalle
            # -------------------------

            detalle, tenencias = parse_fondo_detalle(
                detail_html,
                fondo.id
            )

            detalles.append(detalle)

            # -------------------------
            # factsheet pdf
            # -------------------------

            pdf_url = detalle.factsheet_url

            if pdf_url:

                try:
                    
                    pdf_file = (
                        PDF_DIR /
                        f"{safe_name}_factsheet_{timestamp}.pdf"
                    )
                    download_pdf(
                        pdf_url,
                        pdf_file
                    )
                    print(
                        f"PDF descargado: "
                        f"{pdf_file}"
                    )

                    # -------------------------
                    # extraer texto pdf
                    # -------------------------

                    if SAVE_FACTSHEET_TXT:
                        text = extract_pdf_text(
                            pdf_file
                        )

                        txt_file = (
                            PDF_DIR /
                            f"{safe_name}_factsheet_{timestamp}.txt"
                        )

                        with open(
                            txt_file,
                            "w",
                            encoding="utf-8"
                        ) as f:

                            f.write(text)

                        print(
                            f"TXT generado: "
                            f"{txt_file}"
                        )
                        
                        # -------------------------
                        # parse factsheet
                        # -------------------------
                        
                        factsheet = parse_factsheet(
                            text,
                            fondo.id
                        )

                        factsheets.append(factsheet)

                        print(
                            f"Factsheet parseado: "
                            f"{fondo.nombre}"
                        )

                except Exception as e:

                    print(
                        f"Error procesando "
                        f"factsheet PDF: {e}"
                    )

            # -------------------------
            # cuotapartes
            # -------------------------

            try:
                cuotapartes_html = (
                    get_cuotapartes_html(
                        fondo.id
                    )
                )

                if SAVE_DEBUG_HTML:
                    cuotaparte_html_file = (
                        CUOTAPARTE_DIR /
                        f"{safe_name}_cuotapartes_{timestamp}.html"
                    )

                    with open(
                        cuotaparte_html_file,
                        "w",
                        encoding="utf-8"
                    ) as f:

                        f.write(cuotapartes_html)

                    print(
                        f"HTML cuotapartes generado: "
                        f"{cuotaparte_html_file}"
                    )

                # -------------------------
                # parse cuotapartes
                # -------------------------

                cuotapartes = parse_cuotapartes(
                    cuotapartes_html,
                    fondo.id
                )

                print(
                    f"Cuotapartes encontradas: "
                    f"{len(cuotapartes)}"
                )

                # -------------------------
                # guardar csv cuotapartes
                # -------------------------

                cuotapartes_csv = (
                    CUOTAPARTE_DIR /
                    f"{safe_name}_cuotapartes_{timestamp}.csv"
                )

                save_cuotapartes_csv(
                    cuotapartes,
                    cuotapartes_csv
                )

                print(
                    f"CSV cuotapartes generado: "
                    f"{cuotapartes_csv}"
                )

            except Exception as e:

                print(
                    f"Error procesando "
                    f"cuotapartes: {e}"
                )

            # -------------------------
            # debug
            # -------------------------

            # print(detalle)
            # print(tenencias)

        except Exception as e:

            print(
                f"Error procesando "
                f"{fondo.nombre}: {e}"
            )

    # -------------------------
    # guardar csv detalle & factsheets
    # -------------------------

    if detalles:

        detail_csv_file = (
            DETAIL_DIR /
            f"detalles_{timestamp}.csv"
        )

        save_detail_csv(
            detalles,
            detail_csv_file
        )

        print(
            f"\nCSV detalle generado: "
            f"{detail_csv_file}"
        )
        
    if factsheets:

        factsheet_csv_file = (
            PDF_DIR /
            f"factsheets_{timestamp}.csv"
        )

        save_factsheets_csv(
            factsheets,
            factsheet_csv_file
        )

        print(
            f"\nCSV factsheets generado: "
            f"{factsheet_csv_file}"
        )


if __name__ == "__main__":
    main()