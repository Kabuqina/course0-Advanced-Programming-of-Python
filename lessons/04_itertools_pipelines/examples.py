"""Lesson 04 可运行示例：lru_cache、partial、singledispatch、itertools 组合。

直接运行：``python lessons/04_itertools_pipelines/examples.py``
"""

from __future__ import annotations

import functools
import itertools


@functools.lru_cache(maxsize=None)
def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)


def power(base: float, exp: float) -> float:
    return base ** exp


# functools.partial 固定部分参数，生成新函数
square = functools.partial(power, exp=2)
cube = functools.partial(power, exp=3)


@functools.singledispatch
def to_json_scalar(obj):
    raise TypeError(f"unsupported: {type(obj).__name__}")


@to_json_scalar.register
def _(obj: bool):  # 注意：bool 要在 int 之前注册，否则被 int 抢先
    return "true" if obj else "false"


@to_json_scalar.register
def _(obj: int):
    return str(obj)


@to_json_scalar.register
def _(obj: str):
    return f'"{obj}"'


def main() -> None:
    print("factorial(6):", factorial(6))
    print("square(5):", square(5), "cube(3):", cube(3))
    print("to_json_scalar:", to_json_scalar(True), to_json_scalar(7), to_json_scalar("hi"))

    # itertools.chain 把多个可迭代对象串起来惰性遍历
    merged = itertools.chain([1, 2], [3, 4], [5])
    print("chain:", list(merged))

    # itertools.groupby 需要先按 key 排序才能聚合非连续项
    words = ["apple", "banana", "avocado", "blueberry", "cherry"]
    for initial, group in itertools.groupby(sorted(words), key=lambda w: w[0]):
        print(f"  {initial}: {list(group)}")


if __name__ == "__main__":
    main()
