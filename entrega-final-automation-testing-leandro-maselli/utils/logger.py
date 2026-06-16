import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

log_dir = BASE_DIR / "logs"
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_dir / "suite.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    force=True
)

logger = logging.getLogger("talentolab")