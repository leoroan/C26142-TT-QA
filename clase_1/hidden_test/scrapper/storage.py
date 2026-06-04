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

    rows = [asdict(fondo) for fondo in fondos]

    df = pd.DataFrame(rows)

    df.to_csv(filepath, **CSV_OPTIONS)


def save_detail_csv(detalles, filepath):

    rows = [asdict(detalle) for detalle in detalles]

    df = pd.DataFrame(rows)

    df.to_csv(filepath, **CSV_OPTIONS)


def save_cuotapartes_csv(cuotapartes, filepath):

    rows = [asdict(c) for c in cuotapartes]

    df = pd.DataFrame(rows)

    df.to_csv(filepath, **CSV_OPTIONS)


def save_factsheets_csv(factsheets, filepath):

    rows = [asdict(factsheet) for factsheet in factsheets]

    df = pd.DataFrame(rows)

    df.to_csv(filepath, index=False, encoding="utf-8-sig", sep=";", quoting=1)
