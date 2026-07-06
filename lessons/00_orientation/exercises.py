"""Lesson 00 练习：实现下列函数，使 tests/test_00_orientation.py 通过。

这是本课程的“红→绿”入门：先跑测试看到失败，再实现让它通过。做完对照 solutions.py。
"""

from __future__ import annotations

import sys
from pathlib import Path


def greet(name: str) -> str:
    """返回课程欢迎语：``Hello, {name}! Welcome to Course0.``

    这是“修改一个简单函数让测试通过”的练习。
    """
    raise NotImplementedError


def python_at_least(major: int, minor: int) -> bool:
    """判断当前解释器版本是否 >= (major, minor)。

    提示：sys.version_info 可直接与元组比较。
    """
    raise NotImplementedError


def environment_report() -> dict[str, str]:
    """返回一份简单环境报告，至少包含 python_version / executable / cwd。"""
    return {
        "python_version": sys.version.split()[0],
        "executable": sys.executable,
        "cwd": str(Path.cwd()),
    }
