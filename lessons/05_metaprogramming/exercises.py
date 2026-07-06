"""模块 5 练习：实现描述符与子类注册，使对应测试通过。

做完后对照 solutions.py。
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Type

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


class Typed:
    """类型校验描述符：赋值类型不符抛 TypeError。

    提示：用 __set_name__ 记住属性名，值存到 "_" + name。
    """

    def __init__(self, expected_type: type) -> None:
        self.expected_type = expected_type

    def __set_name__(self, owner: type, name: str) -> None:
        raise NotImplementedError

    def __get__(self, obj, owner=None):
        raise NotImplementedError

    def __set__(self, obj, value) -> None:
        raise NotImplementedError


class Positive:
    """正数校验描述符：非数字抛 TypeError，<= 0 抛 ValueError。"""

    def __set_name__(self, owner: type, name: str) -> None:
        raise NotImplementedError

    def __get__(self, obj, owner=None):
        raise NotImplementedError

    def __set__(self, obj, value) -> None:
        raise NotImplementedError


class Plugin:
    """基类：子类定义时应自动注册到 Plugin.registry（键为类名）。"""

    registry: Dict[str, Type["Plugin"]] = {}

    def __init_subclass__(cls, **kwargs) -> None:
        raise NotImplementedError


class Book:
    """用上面的描述符做字段校验（实现描述符后本类即可工作）。"""

    title = Typed(str)
    author = Typed(str)
    year = Typed(int)
    price = Positive()

    def __init__(self, title: str, author: str, year: int, price: float) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.price = price


def make_books(path: str | Path) -> List[Book]:
    """从 books.json 构造 Book 列表（描述符会在构造时校验）。"""
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    return [
        Book(b["title"], b["author"], int(b["year"]), float(b["price"]))
        for b in raw
    ]
