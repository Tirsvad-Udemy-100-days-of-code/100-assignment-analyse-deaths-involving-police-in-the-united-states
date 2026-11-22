"""@brief Locate the data files and screenshot files of the project."""

from pathlib import Path

from fatal_force.constants import (
    DATA_DIR_NAME,
    SCREENSHOT_DIR,
    SCREENSHOT_PREFIX,
    SCREENSHOT_SUFFIX,
)

_REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
_STEP_DIGITS = 2


def _resolve_root(root: Path | None) -> Path:
    """@brief Choose the root directory to use.

    @param root An explicit root, or None for the repository root.
    @return The explicit root when given, else the repository root.
    """
    return _REPOSITORY_ROOT if root is None else root


def data_file(name: str, root: Path | None = None) -> Path:
    """@brief Build the path of a file in the data directory.

    @param name The file name inside the data directory.
    @param root The root directory; defaults to the repository root.
    @return The path root/DATA_DIR_NAME/name.
    """
    return _resolve_root(root) / DATA_DIR_NAME / name


def screenshot_file(step: int, slug: str, root: Path | None = None) -> Path:
    """@brief Build the path of the screenshot of an analysis step.

    @param step The step number, 1 or higher.
    @param slug A short name for the step, used in the file name.
    @param root The root directory; defaults to the repository root.
    @return The path root/docs/screenshots/step-NN-slug.png.
    @throws ValueError When step is lower than 1.
    """
    if step < 1:
        message = f"step must be 1 or higher, got {step}"
        raise ValueError(message)
    number = str(step).zfill(_STEP_DIGITS)
    file_name = f"{SCREENSHOT_PREFIX}{number}-{slug}{SCREENSHOT_SUFFIX}"
    return _resolve_root(root) / SCREENSHOT_DIR / file_name
