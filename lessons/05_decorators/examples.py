"""Lesson 05 可运行示例：闭包、计时装饰器、带参装饰器。

直接运行：``python lessons/05_decorators/examples.py``
"""

from __future__ import annotations

import functools
import time


def make_multiplier(factor):
    """闭包：内层函数记住 factor。"""
    def multiply(x):
        return x * factor
    return multiply


def timed(func):
    """计时装饰器：打印耗时并返回原结果。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed*1000:.2f} ms")
        return result
    return wrapper


def repeat(n):
    """带参装饰器：把返回值重复 n 次组成列表。"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(n)]
        return wrapper
    return decorator


@timed
@repeat(3)
def roll():
    return 4


def main() -> None:
    triple = make_multiplier(3)
    print("closure triple(5):", triple(5))
    print("repeat+timed roll():", roll())
    print("wraps kept name:", roll.__name__)  # 'roll'，得益于 functools.wraps


if __name__ == "__main__":
    main()
