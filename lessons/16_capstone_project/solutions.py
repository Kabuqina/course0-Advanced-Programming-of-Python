"""Lesson 16 参考解答（选题 A：Course Resource Pack Checker 雏形）。

CLI: ``python -m lessons.16_capstone_project.solutions --root lessons --format markdown``
或   ``python lessons/16_capstone_project/solutions.py --root lessons``
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Dict, Iterator, List

logger = logging.getLogger(__name__)

REQUIRED_FILES = (
    "metadata.yml",
    "README.md",
    "examples.py",
    "exercises.py",
    "solutions.py",
)


def iter_lesson_dirs(lessons_root: str | Path) -> Iterator[Path]:
    """惰性产出 lessons_root 下的子目录（按名字排序）。"""
    root = Path(lessons_root)
    for path in sorted(root.iterdir()):
        if path.is_dir() and not path.name.startswith("_"):
            yield path


def check_lesson(lesson_dir: str | Path, required=REQUIRED_FILES) -> List[str]:
    """返回 lesson_dir 中缺失的必需文件名列表（保持 required 顺序）。"""
    directory = Path(lesson_dir)
    return [name for name in required if not (directory / name).exists()]


def check_course(lessons_root: str | Path, required=REQUIRED_FILES) -> Dict[str, List[str]]:
    """遍历每个 lesson 目录，返回 {lesson_name: [缺失文件...]}。"""
    report: Dict[str, List[str]] = {}
    for lesson_dir in iter_lesson_dirs(lessons_root):
        missing = check_lesson(lesson_dir, required)
        report[lesson_dir.name] = missing
        if missing:
            logger.warning("%s 缺失 %d 个文件: %s", lesson_dir.name, len(missing), missing)
    return report


def format_report(report: Dict[str, List[str]], fmt: str = "markdown") -> str:
    """把结果格式化为 markdown 表格或纯文本。"""
    if fmt == "markdown":
        lines = ["| Lesson | 状态 | 缺失文件 |", "|---|---|---|"]
        for name, missing in report.items():
            status = "✅ OK" if not missing else f"❌ 缺 {len(missing)}"
            lines.append(f"| {name} | {status} | {', '.join(missing) or '-'} |")
        return "\n".join(lines)
    if fmt == "plain":
        lines = []
        for name, missing in report.items():
            lines.append(f"{name}: {'OK' if not missing else ', '.join(missing)}")
        return "\n".join(lines)
    raise ValueError(f"unknown format: {fmt!r}")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Course Resource Pack Checker")
    parser.add_argument("--root", default="lessons", help="lessons 根目录")
    parser.add_argument("--format", default="markdown", choices=["markdown", "plain"])
    return parser


def main(argv: List[str] | None = None) -> int:
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args(argv)
    report = check_course(args.root)
    print(format_report(report, fmt=args.format))
    # 有任何缺失则返回非零退出码，便于 CI。
    return 1 if any(report.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
