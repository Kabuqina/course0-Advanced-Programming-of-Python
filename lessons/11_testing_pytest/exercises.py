"""Lesson 11 练习：实现下列函数，使 tests/test_11_testing_pytest.py 通过。

先阅读那个测试文件——它演示了 parametrize / raises / fixture / tmp_path。
做完后对照 solutions.py。
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, List

_TRUE = {"true", "yes", "1", "on", "y"}
_FALSE = {"false", "no", "0", "off", "n"}


def parse_bool(text: str) -> bool:
    """把字符串解析为布尔值（大小写不敏感、忽略首尾空白）。

    True 集合：true/yes/1/on/y；False 集合：false/no/0/off/n。
    其它输入抛 ValueError。
    """
    raise NotImplementedError


def running_total(numbers: Iterable[float]) -> List[float]:
    """返回累计和列表。running_total([1, 2, 3]) -> [1, 3, 6]；空输入 -> []。"""
    raise NotImplementedError


def word_count(path: str | Path) -> Dict[str, int]:
    """统计文本文件中每个词（按空白分割）出现次数。"""
    raise NotImplementedError
