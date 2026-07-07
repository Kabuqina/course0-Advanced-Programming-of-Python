"""Lesson 09 参考解答：类型标注、数据类与协议。"""

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Protocol, Union, runtime_checkable

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


@dataclass(frozen=True, order=True)
class Money:
    """不可变货币值，以「分」为单位存储，避免浮点误差。"""

    cents: int
    currency: str = "CNY"

    def __post_init__(self) -> None:
        if self.cents < 0:
            raise ValueError("cents must be >= 0")
        if len(self.currency) != 3:
            raise ValueError("currency must be a 3-letter code")

    def plus(self, other: "Money") -> "Money":
        if other.currency != self.currency:
            raise ValueError("cannot add different currencies")
        return Money(self.cents + other.cents, self.currency)

    def __str__(self) -> str:
        return f"{self.cents / 100:.2f} {self.currency}"


@dataclass
class Employee:
    id: int
    name: str
    department: str
    salary: int

    @classmethod
    def from_row(cls, row: Dict[str, str]) -> "Employee":
        return cls(
            id=int(row["id"]),
            name=row["name"],
            department=row["department"],
            salary=int(row["salary"]),
        )


def load_employees(path: Union[str, Path]) -> List[Employee]:
    """读取 employees.csv 为 Employee 列表。"""
    with open(path, encoding="utf-8", newline="") as f:
        return [Employee.from_row(row) for row in csv.DictReader(f)]


def by_department(employees: Iterable[Employee]) -> Dict[str, List[Employee]]:
    """按部门分组。"""
    groups: Dict[str, List[Employee]] = {}
    for emp in employees:
        groups.setdefault(emp.department, []).append(emp)
    return groups


def highest_paid(employees: Iterable[Employee]) -> Employee:
    """返回薪资最高的员工；空集合抛 ValueError。"""
    emps = list(employees)
    if not emps:
        raise ValueError("no employees")
    return max(emps, key=lambda e: e.salary)


@runtime_checkable
class Priced(Protocol):
    """任何拥有数值 price 属性的对象。"""

    price: float


def total_value(items: Iterable[Priced]) -> float:
    """对一组「有 price 的对象」求和。"""
    return sum(item.price for item in items)


if __name__ == "__main__":
    wallet = Money(1050).plus(Money(200))
    print("money:", wallet)  # 12.50 CNY
    staff = load_employees(DATA_DIR / "employees.csv")
    print("headcount by dept:", {k: len(v) for k, v in by_department(staff).items()})
    print("highest paid:", highest_paid(staff).name)
