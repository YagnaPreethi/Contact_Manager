"""JSON storage utilities for the library application."""

import json
import os
import tempfile
from pathlib import Path
from typing import Any


DATA_DIR = Path(__file__).resolve().parent / "data"


def load_json(filename: str) -> list[dict[str, Any]]:
    """Load a JSON list from the data directory."""
    path = DATA_DIR / filename

    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{filename} contains invalid JSON.") from exc

    if not isinstance(data, list):
        raise ValueError(f"{filename} must contain a JSON list.")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError(f"{filename} must contain a list of objects.")

    return data


def save_json(filename: str, records: list[dict[str, Any]]) -> None:
    """Save JSON data safely using a temporary file."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    path = DATA_DIR / filename

    file_descriptor, temporary_name = tempfile.mkstemp(
        dir=DATA_DIR,
        prefix=f".{path.stem}_",
        suffix=".tmp",
    )

    try:
        with os.fdopen(
            file_descriptor, "w", encoding="utf-8"
        ) as file:
            json.dump(records, file, indent=4)
            file.write("\n")

        os.replace(temporary_name, path)

    except Exception:
        if os.path.exists(temporary_name):
            os.remove(temporary_name)
        raise