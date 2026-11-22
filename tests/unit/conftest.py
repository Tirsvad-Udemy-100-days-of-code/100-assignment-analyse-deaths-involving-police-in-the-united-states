from collections.abc import Callable
from pathlib import Path

import pytest

WriteCsv = Callable[[str, list[str]], Path]


@pytest.fixture
def write_csv(tmp_path: Path) -> WriteCsv:
    """Write lines as a cp1252 file with bare CR terminators."""

    def write(name: str, lines: list[str]) -> Path:
        path = tmp_path / name
        path.write_bytes("\r".join(lines).encode("cp1252"))
        return path

    return write
