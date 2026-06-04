from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SNAPSHOTS_DIR = BASE_DIR / "snapshots"

LIST_DIR = SNAPSHOTS_DIR / "list"
DETAIL_DIR = SNAPSHOTS_DIR / "detail"
PDF_DIR = SNAPSHOTS_DIR / "pdf"
CUOTAPARTE_DIR = SNAPSHOTS_DIR / "cuotapartes"

DIRECTORIES = [
    LIST_DIR,
    DETAIL_DIR,
    PDF_DIR,
    CUOTAPARTE_DIR,
]


def ensure_directories():
    for directory in DIRECTORIES:
        directory.mkdir(
            parents=True,
            exist_ok=True
        )
        
def get_latest_csv(
    directory,
    pattern="*.csv"
):
    files = sorted(
        directory.glob(pattern),
        key=lambda f: f.stat().st_mtime,
        reverse=True
    )

    if not files:
        raise FileNotFoundError(
            f"No se encontraron CSVs en {directory}"
        )

    return files[0]