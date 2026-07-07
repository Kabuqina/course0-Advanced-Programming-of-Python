"""模块 7 练习：实现下列函数，使对应测试通过。

做完后对照 solutions.py。提示：lru_cache、reduce、singledispatch、islice/accumulate/groupby。
"""

from __future__ import annotations

import functools  # noqa: F401
import itertools  # noqa: F401
from typing import Callable, Iterable, Iterator, List, Tuple, TypeVar

T = TypeVar("T")


def fib(n: int) -> int:
    """记忆化斐波那契。n < 0 抛 ValueError。

    提示：给函数加 @functools.lru_cache(maxsize=None)。
    """
    raise NotImplementedError


def compose(*funcs: Callable) -> Callable:
    """从右到左组合函数：compose(f, g)(x) == f(g(x))。

    提示：functools.reduce over reversed(funcs)。
    """
    raise NotImplementedError


def describe(obj) -> str:
    """按类型分派：int -> "int: N"，str -> "str of length N"，
    list -> "list of N items"，其余 -> "object: repr"。

    提示：functools.singledispatch + register。
    """
    raise NotImplementedError


def chunked(iterable: Iterable[T], size: int) -> Iterator[List[T]]:
    """按 size 惰性切块；size < 1 抛 ValueError。提示：itertools.islice。"""
    raise NotImplementedError


def running_total(numbers: Iterable[float]) -> List[float]:
    """前缀和。提示：itertools.accumulate。"""
    raise NotImplementedError


def group_consecutive(items: Iterable[T]) -> List[Tuple[T, int]]:
    """连续相同元素聚合为 (值, 次数)。提示：itertools.groupby。"""
    raise NotImplementedError
