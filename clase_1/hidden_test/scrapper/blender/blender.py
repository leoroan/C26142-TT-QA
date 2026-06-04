import pandas as pd

from hidden_test.scrapper.blender.loaders import (
    load_fondos,
    load_detalles,
    load_factsheets,
    load_cuotapartes,
)

from hidden_test.scrapper.blender.cleaners import (
    clean_fondos,
    clean_detalles,
    clean_factsheets,
    clean_cuotapartes,
)

from hidden_test.scrapper.blender.joins import build_master_dataset


def main():

    fondos = clean_fondos(
        load_fondos()
    )

    detalles = clean_detalles(
        load_detalles()
    )

    factsheets = clean_factsheets(
        load_factsheets()
    )

    cuotapartes = clean_cuotapartes(
        load_cuotapartes()
    )

    master = build_master_dataset(
        fondos,
        detalles,
        factsheets,
        cuotapartes,
    )

    master.to_csv(
        "dataset_final.csv",
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )

    print(master.info())
    print(master.head())


if __name__ == "__main__":
    main()