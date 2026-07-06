"""模块 1 练习：实现下列函数，使 tests/test_01_iterators_generators.py 通过。

提示：全部用生成器/惰性方式实现，不要一次性把文件读进内存。
做完后可对照 solutions.py。
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, Iterable, Iterator, List

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def read_ints(path: str | Path) -> Iterator[int]:
    """惰性产出文件中每行的整数，跳过空行。"""
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield int(line)


def running_max(iterable: Iterable[int]) -> Iterator[int]:
    """产出到目前为止遇到的最大值。

    例：running_max([3, 1, 4, 1, 5]) -> 3, 3, 4, 4, 5
    """
    raise NotImplementedError


def chunk(iterable: Iterable, size: int) -> Iterator[List]:
    """把可迭代对象按固定大小切块；最后一块可能不足 size。

    例：list(chunk([1,2,3,4,5], 2)) -> [[1,2],[3,4],[5]]
    size <= 0 时抛 ValueError。
    """
    raise NotImplementedError


def sales_rows(path: str | Path) -> Iterator[Dict[str, str]]:
    """惰性把 sales.csv 每行解析为字典（提示：csv.DictReader）。"""
    with open(path, newline="", encoding="utf-8") as f:
        yield from csv.DictReader(f)


def revenue_by_region(path: str | Path) -> Dict[str, float]:
    """按地区汇总营收（units * price），结果保留两位小数。

    使用 sales_rows 的惰性行流，不要把整个文件读进列表。
    """
    raise NotImplementedError
