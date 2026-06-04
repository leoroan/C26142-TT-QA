from fetcher import get_html
from parsers.parser import parse_fondos


def obtener_fondos():
    html = get_html()

    fondos = parse_fondos(html)

    return html, fondos