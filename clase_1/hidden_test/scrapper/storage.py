import pandas as pd
from dataclasses import asdict


def save_csv(fondos, filepath):

    rows = [
        asdict(fondo)
        for fondo in fondos
    ]

    df = pd.DataFrame(rows)

    df.to_csv(
        filepath,
        index=False,
        encoding="utf-8-sig"
    )