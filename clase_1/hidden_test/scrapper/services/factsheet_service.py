from pathlib import Path

from fetcher import download_pdf

from parsers.parser_pdf import (
    extract_pdf_text,
)

from parsers.parser_factsheet import (
    parse_factsheet,
)

from config import (
    SAVE_FACTSHEET_TXT,
    SAVE_FACTSHEET_PDF,
)


def safe_delete(path: Path):
    try:

        if path.exists():
            path.unlink()

    except Exception as e:

        print(f"No se pudo borrar " f"{path}: {e}")


def procesar_factsheet(pdf_url, pdf_file, txt_file, fondo_id, fondo_nombre):
    try:

        download_pdf(pdf_url, pdf_file)

        text = extract_pdf_text(pdf_file)

        with open(txt_file, "w", encoding="utf-8") as f:

            f.write(text)

        factsheet = parse_factsheet(text, fondo_id, fondo_nombre)

        return factsheet

    finally:

        if not SAVE_FACTSHEET_PDF:
            safe_delete(pdf_file)

        if not SAVE_FACTSHEET_TXT:
            safe_delete(txt_file)
