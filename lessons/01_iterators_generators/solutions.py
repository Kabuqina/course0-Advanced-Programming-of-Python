"""模块 1 参考解答：迭代器与生成器。"""

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
    """产出到目前为止遇到的最大值。"""
    current = None
    for value in iterable:
        current = value if current is None else max(current, value)
        yield current


def take(iterable: Iterable, k: int) -> List:
    """取前 k 个元素（对无限生成器也安全）。"""
    out: List = []
    for i, value in enumerate(iterable):
        if i >= k:
            break
        out.append(value)
    return out


def chunk(iterable: Iterable, size: int) -> Iterator[List]:
    """把可迭代对象按固定大小切块；最后一块可能不足 size。"""
    if size <= 0:
        raise ValueError("size must be positive")
    batch: List = []
    for value in iterable:
        batch.append(value)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch


def sales_rows(path: str | Path) -> Iterator[Dict[str, str]]:
    """惰性把 sales.csv 每行解析为字典。"""
    with open(path, newline="", encoding="utf-8") as f:
        yield from csv.DictReader(f)


def revenue_by_region(path: str | Path) -> Dict[str, float]:
    """按地区汇总营收（units * price），基于惰性行流。"""
    totals: Dict[str, float] = {}
    for row in sales_rows(path):
        revenue = int(row["units"]) * float(row["price"])
        totals[row["region"]] = round(totals.get(row["region"], 0.0) + revenue, 2)
    return totals


if __name__ == "__main__":
    print("running_max:", take(running_max(read_ints(DATA_DIR / "numbers.txt")), 5))
    print("chunks of 4:", take(chunk(read_ints(DATA_DIR / "numbers.txt"), 4), 2))
    print("revenue_by_region:", revenue_by_region(DATA_DIR / "sales.csv"))
