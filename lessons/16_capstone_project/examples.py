"""Lesson 16 可运行示例：对本仓库的 lessons/ 跑一遍资源包检查（选题 A 雏形）。

直接运行：``python lessons/16_capstone_project/examples.py``
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from solutions import check_course, format_report  # noqa: E402

LESSONS_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    report = check_course(LESSONS_ROOT)
    print(format_report(report, fmt="markdown"))


if __name__ == "__main__":
    main()
