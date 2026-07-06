"""Lesson 16 练习骨架（选题 A：Course Resource Pack Checker）。

实现下列函数，使 tests/test_16_capstone_project.py 通过；再自行扩展（JSON 输出、
metadata 字段校验、CI 退出码等）。做完对照 solutions.py。
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

REQUIRED_FILES = (
    "metadata.yml",
    "README.md",
    "examples.py",
    "exercises.py",
    "solutions.py",
)


def check_lesson(lesson_dir: str | Path, required=REQUIRED_FILES) -> List[str]:
    """返回 lesson_dir 中缺失的必需文件名列表（按 required 顺序）。"""
    raise NotImplementedError


def check_course(lessons_root: str | Path, required=REQUIRED_FILES) -> Dict[str, List[str]]:
    """遍历 lessons_root 下每个子目录，返回 {lesson_name: [缺失文件...]}。"""
    raise NotImplementedError


def format_report(report: Dict[str, List[str]], fmt: str = "markdown") -> str:
    """把 check_course 的结果格式化为字符串（markdown / plain）。"""
    raise NotImplementedError
