"""Lesson 01 可运行示例：身份/相等、可变默认参数、浅拷贝/深拷贝、作用域。

直接运行：``python lessons/01_objects_names_mutability/examples.py``
"""

from __future__ import annotations

import copy


def identity_demo() -> None:
    a = [1, 2, 3]
    b = a               # 同一对象
    c = [1, 2, 3]       # 值相等但不同对象
    print("a is b:", a is b, "| a == c:", a == c, "| a is c:", a is c)


def mutable_default_bug() -> None:
    def bad(grade, scores=[]):      # 陷阱：默认值只创建一次
        scores.append(grade)
        return scores

    print("bad(90):", bad(90))
    print("bad(80):", bad(80), "  <- 意外共享")


def copy_demo() -> None:
    nested = {"scores": [90, 80]}
    shallow = copy.copy(nested)
    deep = copy.deepcopy(nested)
    nested["scores"].append(70)
    print("shallow 受影响:", shallow["scores"])   # [90, 80, 70]
    print("deep 独立:", deep["scores"])           # [90, 80]


def scope_demo() -> None:
    total = 0

    def add(x):
        nonlocal total          # 修改外层名字，而非新建局部
        total += x

    add(3)
    add(4)
    print("closure total:", total)


def main() -> None:
    identity_demo()
    mutable_default_bug()
    copy_demo()
    scope_demo()


if __name__ == "__main__":
    main()
