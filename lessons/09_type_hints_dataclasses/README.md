# Lesson 09 · 类型标注、数据类与协议

> 迁移自旧 `06_dataclasses_typing`（对齐 `course_structure.md` 的 Lesson 09 编号）。

## 目标
- 用 `@dataclass` 自动生成 `__init__` / `__repr__` / `__eq__`
- 掌握 `frozen=True`（不可变）、`order=True`（可比较）、`field(default_factory=...)`
- 在 `__post_init__` 里做校验，保证对象一创建就合法
- 用 `typing.Protocol` 表达「结构化鸭子类型」（只关心有没有某属性/方法）

## 要点

`@dataclass` 把「一堆字段 + 样板方法」浓缩成声明式写法：

```python
from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class Money:
    cents: int              # 以「分」为单位，避免浮点误差
    currency: str = "CNY"

    def __post_init__(self):
        if self.cents < 0:
            raise ValueError("cents must be >= 0")
```

- `frozen=True` 后实例不可变（改属性抛 `FrozenInstanceError`），因此可哈希、可做字典键。
- `order=True` 按字段元组顺序生成 `<`、`>` 等比较；配合 `max(..., key=...)` 很顺手。
- 可变默认值必须用 `field(default_factory=list)`，不能直接写 `= []`。

**Protocol**：不需要显式继承，只要「长得像」就算匹配，适合解耦：

```python
from typing import Protocol

class Priced(Protocol):
    price: float

def total(items: list[Priced]) -> float:
    return sum(i.price for i in items)
```

## 本模块练习（见 `exercises.py`）
1. `Money`：不可变货币值，`plus` 只允许同币种相加，`__post_init__` 校验
2. `Employee` + `load_employees`：把 `data/employees.csv` 读成数据类列表
3. `by_department` / `highest_paid`：按部门分组、取薪资最高者
4. `total_value`：基于 `Priced` 协议对任意「有 price 的对象」求和

运行示例：`python lessons/06_dataclasses_typing/examples.py`
