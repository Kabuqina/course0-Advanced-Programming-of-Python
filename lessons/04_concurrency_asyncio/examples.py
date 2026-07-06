"""模块 4 可运行示例：并发 vs 串行耗时对比、信号量限流。

直接运行：``python lessons/04_concurrency_asyncio/examples.py``
"""

from __future__ import annotations

import asyncio
import time


async def work(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return name


async def sequential() -> float:
    start = time.perf_counter()
    await work("a", 0.05)
    await work("b", 0.05)
    await work("c", 0.05)
    return time.perf_counter() - start


async def concurrent() -> float:
    start = time.perf_counter()
    await asyncio.gather(work("a", 0.05), work("b", 0.05), work("c", 0.05))
    return time.perf_counter() - start


async def main() -> None:
    seq = await sequential()
    con = await concurrent()
    print(f"串行耗时: {seq*1000:.0f} ms（约三段之和）")
    print(f"并发耗时: {con*1000:.0f} ms（约等于最长一段）")


if __name__ == "__main__":
    asyncio.run(main())
