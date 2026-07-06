"""Lesson 00 可运行示例：环境自检与仓库概览。

直接运行：``python lessons/00_orientation/examples.py``
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    print("Python 版本:", sys.version.split()[0])
    print("解释器路径:", sys.executable)
    print("仓库根目录:", ROOT)

    lessons = sorted(p.name for p in (ROOT / "lessons").iterdir() if p.is_dir())
    print("已有 lessons:", lessons)

    data_files = sorted(p.name for p in (ROOT / "data").iterdir() if p.is_file())
    print("data 文件:", data_files)

    print("Python >= 3.10:", sys.version_info >= (3, 10))


if __name__ == "__main__":
    main()
