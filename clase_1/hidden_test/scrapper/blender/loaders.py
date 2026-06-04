import pandas as pd

from hidden_test.scrapper.paths import (
    LIST_DIR,
    DETAIL_DIR,
    PDF_DIR,
    CUOTAPARTE_DIR,
    get_latest_csv,
)


def load_csv(path):

    print(
        f"Cargando: {path}"
    )

    return pd.read_csv(
        path,
        sep=";",
        encoding="utf-8-sig",
    )


def load_fondos():

    path = get_latest_csv(
        LIST_DIR,
        "los_fondos_*.csv"
    )

    return load_csv(path)


def load_detalles():

    path = get_latest_csv(
        DETAIL_DIR,
        "detalles_*.csv"
    )

    return load_csv(path)


def load_factsheets():

    path = get_latest_csv(
        PDF_DIR,
        "factsheets_*.csv"
    )

    return load_csv(path)

def load_cuotapartes():

    files = list(
        CUOTAPARTE_DIR.glob(
            "*_cuotapartes_*.csv"
        )
    )

    if not files:

        raise FileNotFoundError(
            "No se encontraron cuotapartes"
        )

    dfs = []

    for file in files:

        print(
            f"Cargando: {file}"
        )

        df = pd.read_csv(
            file,
            sep=";",
            encoding="utf-8-sig",
        )

        dfs.append(df)

    return pd.concat(
        dfs,
        ignore_index=True
    )