from fetcher import (
    get_cuotapartes_html,
)

from parsers.parser_cuotaparte import (
    parse_cuotapartes,
)


def obtener_cuotapartes(fondo):
    html = get_cuotapartes_html(
        fondo.id
    )

    cuotapartes = parse_cuotapartes(
        html,
        fondo.id,
        fondo.nombre
    )

    return html, cuotapartes