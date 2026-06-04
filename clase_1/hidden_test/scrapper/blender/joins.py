def build_master_dataset(
    fondos,
    detalles,
    factsheets,
    cuotapartes,
):
    df = cuotapartes.copy()

    df = df.merge(
        fondos,
        left_on="fondo_id",
        right_on="id",
        how="left",
        suffixes=("", "_fondo")
    )

    df = df.merge(
        detalles,
        on="fondo_id",
        how="left"
    )

    df = df.merge(
        factsheets,
        on="fondo_id",
        how="left",
        suffixes=("", "_factsheet")
    )

    return df