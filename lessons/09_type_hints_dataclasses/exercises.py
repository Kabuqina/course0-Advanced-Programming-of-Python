"""Lesson 09 练习：实现下列数据类与函数，使对应测试通过。

做完后对照 solutions.py。提示：善用 @dataclass 的 frozen / order 参数，
以及 __post_init__ 做校验。
"""

import csv  # noqa: F401  (load_employees 会用到)
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Protocol, Union, runtime_checkable

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


@dataclass(frozen=True, order=True)
class Money:
    """不可变货币值，以「分」为单位。

    要求：
    - cents < 0 时在 __post_init__ 抛 ValueError
    - currency 必须是 3 位字母代码，否则抛 ValueError
    - plus(other)：同币种相加返回新的 Money，异币种抛 ValueError
    - __str__ 形如 "10.50 CNY"
    """

    cents: int
    currency: str = "CNY"

    def __post_init__(self) -> None:
        raise NotImplementedError

    def plus(self, other: "Money") -> "Money":
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


@dataclass
class Employee:
    id: int
    name: str
    department: str
    salary: int

    @classmethod
    def from_row(cls, row: Dict[str, str]) -> "Employee":
        """从 csv.DictReader 的一行构造 Employee（注意把 id/salary 转成 int）。"""
        raise NotImplementedError


def load_employees(path: str | Path) -> List[Employee]:
    """读取 employees.csv 为 Employee 列表。"""
    with open(path, encoding="utf-8", newline="") as f:
        return [Employee.from_row(row) for row in csv.DictReader(f)]


def by_department(employees: Iterable[Employee]) -> Dict[str, List[Employee]]:
    """按部门分组为 {部门: [员工, ...]}。"""
    raise NotImplementedError


def highest_paid(employees: Iterable[Employee]) -> Employee:
    """返回薪资最高的员工；空集合抛 ValueError。"""
    raise NotImplementedError


@runtime_checkable
class Priced(Protocol):
    price: float


def total_value(items: Iterable[Priced]) -> float:
    """对一组「有 price 的对象」求和。"""
    raise NotImplementedError
