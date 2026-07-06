"""Lesson 11 参考解答：可验证的小函数（供测试演示 pytest 用法）。"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, List

_TRUE = {"true", "yes", "1", "on", "y"}
_FALSE = {"false", "no", "0", "off", "n"}


def parse_bool(text: str) -> bool:
    """把字符串解析为布尔值（大小写不敏感、忽略首尾空白）。"""
    key = text.strip().lower()
    if key in _TRUE:
        return True
    if key in _FALSE:
        return False
    raise ValueError(f"cannot parse boolean from {text!r}")


def running_total(numbers: Iterable[float]) -> List[float]:
    """返回累计和列表。"""
    total = 0.0
    out: List[float] = []
    for n in numbers:
        total += n
        out.append(total)
    return out


def word_count(path: str | Path) -> Dict[str, int]:
    """统计文本文件中每个词出现次数（按空白分割）。"""
    counts: Dict[str, int] = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    print(parse_bool("Yes"), parse_bool("0"))
    print(running_total([1, 2, 3, 4]))
