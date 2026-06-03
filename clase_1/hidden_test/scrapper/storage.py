# import pandas as pd

# from dataclasses import (
#     asdict
# )


# def save_csv(
#     fondos,
#     filepath
# ):

#     rows = [
#         asdict(fondo)
#         for fondo in fondos
#     ]

#     df = pd.DataFrame(rows)

#     df.to_csv(
#         filepath,
#         index=False,
#         encoding="utf-8-sig"
#     )


# def save_detail_csv(
#     detalles,
#     filepath
# ):

#     rows = [
#         asdict(detalle)
#         for detalle in detalles
#     ]

#     df = pd.DataFrame(rows)

#     df.to_csv(
#         filepath,
#         index=False,
#         encoding="utf-8-sig"
#     )


# def save_cuotapartes_csv(
#     cuotapartes,
#     filepath
# ):

#     rows = [
#         asdict(cuotaparte)
#         for cuotaparte in cuotapartes
#     ]

#     df = pd.DataFrame(rows)

#     # opcional:
#     # ordenar por fecha ascendente

#     if "fecha" in df.columns:

#         df = df.sort_values(
#             by="fecha"
#         )

#     df.to_csv(
#         filepath,
#         index=False,
#         encoding="utf-8-sig"
#     )

import csv

import pandas as pd

from dataclasses import asdict


CSV_OPTIONS = {
    "index": False,
    "encoding": "utf-8-sig",
    "sep": ";",
    "quoting": csv.QUOTE_ALL,
}


def save_csv(fondos, filepath):

    rows = [
        asdict(fondo)
        for fondo in fondos
    ]

    df = pd.DataFrame(rows)

    df.to_csv(
        filepath,
        **CSV_OPTIONS
    )


def save_detail_csv(detalles, filepath):

    rows = [
        asdict(detalle)
        for detalle in detalles
    ]

    df = pd.DataFrame(rows)

    df.to_csv(
        filepath,
        **CSV_OPTIONS
    )


def save_cuotapartes_csv(cuotapartes, filepath):

    rows = [
        asdict(c)
        for c in cuotapartes
    ]

    df = pd.DataFrame(rows)

    df.to_csv(
        filepath,
        **CSV_OPTIONS
    )