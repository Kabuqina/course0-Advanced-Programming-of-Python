"""Lesson 00 参考解答：课程导入与仓库运行。"""

from __future__ import annotations

import sys
from pathlib import Path


def greet(name: str) -> str:
    """返回课程欢迎语。"""
    return f"Hello, {name}! Welcome to Course0."


def python_at_least(major: int, minor: int) -> bool:
    """判断当前解释器版本是否 >= (major, minor)。"""
    return sys.version_info >= (major, minor)


def environment_report() -> dict[str, str]:
    """返回一份简单环境报告，便于写 environment_check.md。"""
    return {
        "python_version": sys.version.split()[0],
        "executable": sys.executable,
        "cwd": str(Path.cwd()),
    }


if __name__ == "__main__":
    print(greet("学员"))
    print("python>=3.10:", python_at_least(3, 10))
    for key, value in environment_report().items():
        print(f"{key}: {value}")
