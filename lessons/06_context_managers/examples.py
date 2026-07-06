"""Lesson 06 可运行示例：类式与生成器式上下文管理器，异常安全。

直接运行：``python lessons/06_context_managers/examples.py``
"""

from __future__ import annotations

import contextlib


class Guard:
    """演示 __exit__ 无论是否异常都会执行。"""

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"enter {self.name}")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"exit {self.name} (exc={exc_type.__name__ if exc_type else None})")
        return False


@contextlib.contextmanager
def tag(name):
    print(f"<{name}>")
    try:
        yield
    finally:
        print(f"</{name}>")


def main() -> None:
    with Guard("outer"):
        with tag("body"):
            print("doing work")

    # __exit__ 仍会运行，即使块内抛异常（这里用 suppress 演示不崩溃）
    with contextlib.suppress(ValueError):
        with Guard("risky"):
            raise ValueError("boom")
    print("continued after handled exception")


if __name__ == "__main__":
    main()
