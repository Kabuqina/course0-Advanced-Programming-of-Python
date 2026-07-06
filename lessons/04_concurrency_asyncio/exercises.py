"""模块 4 练习：实现下列协程，使对应测试通过。

测试用 pytest-asyncio（asyncio_mode=auto）。做完后对照 solutions.py。
"""

from __future__ import annotations

import asyncio  # noqa: F401
import json
from pathlib import Path
from typing import Awaitable, Callable, Dict, List

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_books(path: str | Path) -> List[Dict]:
    """同步读取 books.json。"""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


async def fetch_book(book: Dict, delay: float = 0.005) -> Dict:
    """模拟异步抓取，返回 {"title", "price": float}。"""
    await asyncio.sleep(delay)
    return {"title": book["title"], "price": float(book["price"])}


async def fetch_all(books: List[Dict], delay: float = 0.005) -> List[Dict]:
    """并发抓取所有书并保持顺序（提示：asyncio.gather）。"""
    raise NotImplementedError


async def total_price(books: List[Dict], delay: float = 0.005) -> float:
    """并发抓取后汇总价格，保留两位小数。"""
    raise NotImplementedError


async def bounded_gather(
    factories: List[Callable[[], Awaitable]], limit: int
) -> List:
    """带并发上限运行一批协程工厂（提示：asyncio.Semaphore）。limit < 1 抛 ValueError。"""
    raise NotImplementedError
