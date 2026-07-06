"""模块 4 参考解答：并发与 asyncio。"""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Awaitable, Callable, Dict, List

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_books(path: str | Path) -> List[Dict]:
    """同步读取 books.json（I/O 很小，示例中不异步化文件读取）。"""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


async def fetch_book(book: Dict, delay: float = 0.005) -> Dict:
    """模拟异步抓取一本书的详情。"""
    await asyncio.sleep(delay)
    return {"title": book["title"], "price": float(book["price"])}


async def fetch_all(books: List[Dict], delay: float = 0.005) -> List[Dict]:
    """并发抓取所有书，保持输入顺序（gather 保序）。"""
    return await asyncio.gather(*(fetch_book(b, delay) for b in books))


async def total_price(books: List[Dict], delay: float = 0.005) -> float:
    """并发抓取后汇总价格，保留两位小数。"""
    fetched = await fetch_all(books, delay)
    return round(sum(item["price"] for item in fetched), 2)


async def bounded_gather(
    factories: List[Callable[[], Awaitable]], limit: int
) -> List:
    """带并发上限地运行一批协程。

    传入的是**协程工厂**（可调用，返回协程），以避免协程被重复 await。
    """
    if limit < 1:
        raise ValueError("limit must be >= 1")
    semaphore = asyncio.Semaphore(limit)

    async def run(factory: Callable[[], Awaitable]):
        async with semaphore:
            return await factory()

    return await asyncio.gather(*(run(f) for f in factories))


async def _demo() -> None:
    books = load_books(DATA_DIR / "books.json")
    titles = [b["title"] for b in await fetch_all(books)]
    print("fetched:", len(titles), "books")
    print("total price:", await total_price(books))
    results = await bounded_gather(
        [lambda i=i: fetch_book(books[i]) for i in range(len(books))], limit=3
    )
    print("bounded results:", len(results))


if __name__ == "__main__":
    asyncio.run(_demo())
