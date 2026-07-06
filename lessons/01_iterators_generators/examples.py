"""模块 1 可运行示例：迭代协议、生成器、惰性管道。

直接运行：``python lessons/01_iterators_generators/examples.py``
"""

from __future__ import annotations

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


class Countdown:
    """手写迭代器：演示 __iter__ / __next__ / StopIteration。"""

    def __init__(self, n: int) -> None:
        self.n = n

    def __iter__(self) -> "Countdown":
        return self

    def __next__(self) -> int:
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1


def read_ints(path):
    """惰性读整数——一次只在内存中保留一行。"""
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield int(line)


def main() -> None:
    print("手写迭代器 Countdown(3):", list(Countdown(3)))

    # 惰性管道：过滤 -> 平方，直到 list() 才真正消费。
    nums = read_ints(DATA_DIR / "numbers.txt")
    evens = (n for n in nums if n % 2 == 0)
    squared = (n * n for n in evens)
    print("偶数的平方:", list(squared))

    # yield from 委托
    def flatten(nested):
        for sub in nested:
            yield from sub

    print("flatten:", list(flatten([[1, 2], [3], [4, 5]])))


if __name__ == "__main__":
    main()
