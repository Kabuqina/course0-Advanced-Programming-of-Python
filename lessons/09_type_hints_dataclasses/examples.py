"""Lesson 09 可运行示例：dataclass 的不可变性、比较、Protocol。

直接运行：``python lessons/09_type_hints_dataclasses/examples.py``
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Protocol


@dataclass(frozen=True, order=True)
class Version:
    """不可变、可比较的语义化版本号。"""

    major: int
    minor: int = 0
    patch: int = 0

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


@dataclass
class Cart:
    """可变默认值必须用 field(default_factory=...)。"""

    items: List[str] = field(default_factory=list)

    def add(self, name: str) -> None:
        self.items.append(name)


class Named(Protocol):
    name: str


def greet_all(people: List[Named]) -> List[str]:
    return [f"hello {p.name}" for p in people]


def main() -> None:
    versions = [Version(1, 2, 0), Version(1, 0, 5), Version(2, 0, 0)]
    print("sorted versions:", [str(v) for v in sorted(versions)])
    print("max version:", str(max(versions)))

    cart = Cart()
    cart.add("book")
    cart.add("pen")
    print("cart items:", cart.items)

    @dataclass
    class User:
        name: str

    print(greet_all([User("Alice"), User("Bob")]))

    try:
        Version(1).major = 9  # frozen -> 报错
    except Exception as exc:  # noqa: BLE001
        print("frozen blocked mutation:", type(exc).__name__)


if __name__ == "__main__":
    main()
