"""模块 5 参考解答：描述符与子类注册。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Type

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


class Typed:
    """类型校验描述符：赋值类型不符抛 TypeError。"""

    def __init__(self, expected_type: type) -> None:
        self.expected_type = expected_type

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name
        self.private = "_" + name

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        return getattr(obj, self.private)

    def __set__(self, obj, value) -> None:
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} expects {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        setattr(obj, self.private, value)


class Positive:
    """正数校验描述符：非数字抛 TypeError，<= 0 抛 ValueError。"""

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name
        self.private = "_" + name

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        return getattr(obj, self.private)

    def __set__(self, obj, value) -> None:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be a number")
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        setattr(obj, self.private, float(value))


def auto_repr(cls: type) -> type:
    """类装饰器：根据实例的公开属性自动生成 __repr__。"""

    def __repr__(self) -> str:
        fields = ", ".join(
            f"{k}={v!r}" for k, v in vars(self).items() if not k.startswith("_")
        )
        return f"{cls.__name__}({fields})"

    cls.__repr__ = __repr__  # type: ignore[method-assign]
    return cls


class Plugin:
    """基类：任何子类在定义时自动注册到 registry。"""

    registry: Dict[str, Type["Plugin"]] = {}

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        Plugin.registry[cls.__name__] = cls


class Book:
    """用描述符做字段校验的领域对象。"""

    title = Typed(str)
    author = Typed(str)
    year = Typed(int)
    price = Positive()

    def __init__(self, title: str, author: str, year: int, price: float) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def __repr__(self) -> str:
        return f"Book({self.title!r}, {self.year})"


def make_books(path: str | Path) -> List[Book]:
    """从 books.json 构造 Book 列表；描述符会在构造时校验字段。"""
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    return [
        Book(b["title"], b["author"], int(b["year"]), float(b["price"]))
        for b in raw
    ]


if __name__ == "__main__":
    books = make_books(DATA_DIR / "books.json")
    print("loaded:", len(books), "books; first:", books[0])

    class JsonPlugin(Plugin):
        pass

    class CsvPlugin(Plugin):
        pass

    print("plugins:", sorted(Plugin.registry))
