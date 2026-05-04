"""
Centralized logging configuration for the extraction pipeline.

Usage in any script:

    from misc.logging_config import setup_logging, get_logger, log_step

    setup_logging(run_name="my_experiment")
    logger = get_logger(__name__)

    with log_step(logger, "Extraction", n_items=1000):
        ...  # work happens here; duration auto-logged on exit

All scripts share:
  - Consistent format with timestamps
  - Automatic log file under logs/<run_name>_<timestamp>.log
  - A run_id for correlating steps within a single pipeline execution
  - Step timing via the log_step context manager
"""

import logging
import time
import uuid
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

_RUN_ID: str = ""
_LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
_CONFIGURED = False

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(
    run_name: str = "pipeline",
    level: int = logging.INFO,
    log_dir: str | Path | None = None,
    console: bool = True,
) -> str:
    """Configure the root logger with console + file handlers.

    Returns the run_id (also accessible via ``get_run_id()``).
    Safe to call multiple times — subsequent calls are no-ops.
    """
    global _RUN_ID, _CONFIGURED
    if _CONFIGURED:
        return _RUN_ID

    _RUN_ID = uuid.uuid4().hex[:8]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    dest = Path(log_dir) if log_dir else _LOG_DIR
    dest.mkdir(parents=True, exist_ok=True)
    log_file = dest / f"{run_name}_{timestamp}_{_RUN_ID}.log"

    root = logging.getLogger()
    root.setLevel(level)

    formatter = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT)

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(level)
    fh.setFormatter(formatter)
    root.addHandler(fh)

    if console:
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        if not root.handlers or not any(
            isinstance(h, logging.StreamHandler)
            and not isinstance(h, logging.FileHandler)
            for h in root.handlers
        ):
            root.addHandler(ch)

    _CONFIGURED = True

    root_logger = logging.getLogger("pipeline")
    root_logger.info(
        "Pipeline run started — run_id=%s  log_file=%s",
        _RUN_ID, log_file,
    )
    return _RUN_ID


def get_run_id() -> str:
    return _RUN_ID


def get_logger(name: str) -> logging.Logger:
    """Return a named logger for consistent filtering."""
    return logging.getLogger(name)


@contextmanager
def log_step(
    logger: logging.Logger, step_name: str, **context,
):
    """Log step start/end with duration and optional counts."""
    pairs = (f"[{k}={v}]" for k, v in context.items())
    ctx_str = "  ".join(pairs) if context else ""
    logger.info("┌─ %s  %s", step_name, ctx_str)
    t0 = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - t0
        if elapsed < 60:
            dur = f"{elapsed:.1f}s"
        elif elapsed < 3600:
            dur = f"{elapsed / 60:.1f}min"
        else:
            dur = f"{elapsed / 3600:.1f}hr"
        logger.info("└─ %s  done in %s", step_name, dur)


def log_counts(
    logger: logging.Logger, label: str, **counts,
):
    """Log a one-line summary of counts."""
    parts = "  ".join(
        f"{k}={v}" for k, v in counts.items()
    )
    logger.info("%s — %s", label, parts)
