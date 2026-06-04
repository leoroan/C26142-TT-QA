from fetcher import get_detail_html
from parsers.parser_detalle import parse_fondo_detalle


def obtener_detalle(fondo):
    detail_html = get_detail_html(
        fondo.url_detalle
    )

    detalle, tenencias = parse_fondo_detalle(
        detail_html,
        fondo.id
    )

    return detail_html, detalle, tenencias