"""模块 7 参考解答：functools 与 itertools。"""

from __future__ import annotations

import functools
import itertools
from typing import Callable, Iterable, Iterator, List, Tuple, TypeVar

T = TypeVar("T")


@functools.lru_cache(maxsize=None)
def fib(n: int) -> int:
    """记忆化斐波那契。n < 0 抛 ValueError。"""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def compose(*funcs: Callable) -> Callable:
    """从右到左组合函数：compose(f, g)(x) == f(g(x))。

    无参数时返回恒等函数。
    """

    def composed(x):
        return functools.reduce(lambda acc, fn: fn(acc), reversed(funcs), x)

    return composed


@functools.singledispatch
def describe(obj) -> str:
    return f"object: {obj!r}"


@describe.register
def _(obj: int) -> str:
    return f"int: {obj}"


@describe.register
def _(obj: str) -> str:
    return f"str of length {len(obj)}"


@describe.register
def _(obj: list) -> str:
    return f"list of {len(obj)} items"


def chunked(iterable: Iterable[T], size: int) -> Iterator[List[T]]:
    """把可迭代对象按 size 惰性切块；size < 1 抛 ValueError。"""
    if size < 1:
        raise ValueError("size must be >= 1")
    it = iter(iterable)
    while True:
        chunk = list(itertools.islice(it, size))
        if not chunk:
            return
        yield chunk


def running_total(numbers: Iterable[float]) -> List[float]:
    """前缀和：[1, 2, 3] -> [1, 3, 6]。"""
    return list(itertools.accumulate(numbers))


def group_consecutive(items: Iterable[T]) -> List[Tuple[T, int]]:
    """把连续相同元素聚合为 (值, 次数)。"""
    return [(key, len(list(group))) for key, group in itertools.groupby(items)]


if __name__ == "__main__":
    print("fib(0..7):", [fib(i) for i in range(8)])
    inc = lambda x: x + 1  # noqa: E731
    dbl = lambda x: x * 2  # noqa: E731
    print("compose(inc, dbl)(5):", compose(inc, dbl)(5))  # 11
    print("describe:", describe(42), "|", describe("abc"), "|", describe([1, 2]))
    print("chunked:", list(chunked(range(1, 6), 2)))
    print("running_total:", running_total([1, 2, 3, 4]))
    print("group_consecutive:", group_consecutive("aaabbc"))
