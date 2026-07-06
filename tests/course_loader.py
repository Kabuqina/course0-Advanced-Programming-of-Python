"""Helper to load a lesson's ``solutions.py`` under a unique module name.

Each lesson dir has its own ``solutions.py`` (same filename), so we load by file
path via importlib to avoid name collisions. Tests validate the reference
solutions; learners implement the mirror API in ``exercises.py``.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "lessons"
DATA = ROOT / "data"


def load(lesson_dir: str, module: str = "solutions") -> ModuleType:
    path = LESSONS / lesson_dir / f"{module}.py"
    name = f"{lesson_dir}__{module}"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader, f"cannot load {path}"
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
