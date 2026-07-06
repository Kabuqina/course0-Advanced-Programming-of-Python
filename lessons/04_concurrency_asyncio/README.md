# 模块 4 · 并发与 asyncio

## 目标
- 理解 **GIL** 及其对线程的影响：I/O 密集用线程/协程，CPU 密集用多进程
- 掌握 `async def` / `await` 与事件循环
- 用 `asyncio.gather` 并发执行协程
- 用 `asyncio.Semaphore` 控制并发上限

## 要点

**GIL（全局解释器锁）**：CPython 同一时刻只允许一个线程执行字节码。因此多线程
无法为纯 CPU 计算带来并行加速——那类任务应使用 `multiprocessing`。但线程/协程对
**I/O 等待**很有效：等待期间可切换去做别的事。

**asyncio** 在单线程上用**协作式**并发：`await` 在等待点把控制权交回事件循环，
其它协程得以推进。

```python
import asyncio

async def fetch(name, delay):
    await asyncio.sleep(delay)     # 模拟 I/O；不阻塞线程
    return name

async def main():
    # 并发运行，总耗时约等于最长的那个，而非求和
    return await asyncio.gather(fetch("a", 0.1), fetch("b", 0.05))

asyncio.run(main())
```

**限流**：用信号量约束同时进行的任务数，避免压垮下游：

```python
sem = asyncio.Semaphore(3)
async def worker(job):
    async with sem:
        return await do(job)
```

## 本模块练习（见 `exercises.py`）
1. `fetch_all`：并发抓取 `data/books.json` 里所有书（`gather`）
2. `total_price`：并发抓取后汇总价格
3. `bounded_gather`：带并发上限地运行一批协程

运行示例：`python lessons/04_concurrency_asyncio/examples.py`
