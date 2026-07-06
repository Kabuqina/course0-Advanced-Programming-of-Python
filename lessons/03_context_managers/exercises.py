"""模块 3 练习：实现下列上下文管理器，使对应测试通过。

做完后对照 solutions.py。
"""

from __future__ import annotations

import contextlib  # noqa: F401
import os  # noqa: F401
from pathlib import Path
from typing import Iterator

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


class Timer:
    """上下文管理器：with 块结束后 .elapsed 为耗时（秒，>= 0）。

    提示：__enter__ 记开始时间并 return self；__exit__ 计算 elapsed 并返回 False。
    """

    def __enter__(self) -> "Timer":
        raise NotImplementedError

    def __exit__(self, exc_type, exc, tb) -> bool:
        raise NotImplementedError


def suppress_errors(*exceptions: type[BaseException]):
    """抑制指定异常类型的上下文管理器（用 contextlib.contextmanager）。

    例：with suppress_errors(ValueError): int("x")  # 不抛出
    """
    raise NotImplementedError


def atomic_write(path: str | Path, encoding: str = "utf-8"):
    """原子写上下文管理器：yield 一个可写文件对象；

    正常退出：把临时文件替换为目标文件（os.replace）。
    异常退出：删除临时文件并重新抛出，目标文件保持原样。
    """
    raise NotImplementedError
