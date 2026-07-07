# Lesson 09 讲义 · 类型标注、数据类与协议

## 1. 为什么需要 dataclass

写一个“只装数据”的类，通常要手写 `__init__`、`__repr__`、`__eq__`、`__hash__` 等样板方法。
`@dataclass` 用声明式语法自动生成它们，把焦点放回**数据语义**上。

```python
from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int = 0
    patch: int = 0

v1 = Version(1, 2, 0)
```

## 2. `frozen`、`order`、`default_factory`

- `frozen=True`：实例创建后不可变，天然可哈希，能做字典键。
- `order=True`：按字段声明顺序自动生成 `<`、`<=`、`>`、`>=`，可直接排序。
- 可变默认值（如 `list`、`dict`）不能直接用 `= []`，必须用 `field(default_factory=list)`，
  否则所有实例会共享同一个可变对象。

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Cart:
    items: List[str] = field(default_factory=list)
```

## 3. `__post_init__` 做运行时校验

类型标注本身通常不在运行时强制检查。如果对象创建时就要保证合法，
可以在 `__post_init__` 里抛异常：

```python
@dataclass(frozen=True)
class Money:
    cents: int
    currency: str = "CNY"

    def __post_init__(self):
        if self.cents < 0:
            raise ValueError("cents must be >= 0")
        if len(self.currency) != 3:
            raise ValueError("currency must be a 3-letter code")
```

## 4. `typing.Protocol`：结构化鸭子类型

传统继承要求“是一个（is-a）”；Protocol 只要求“长得像”。只要对象有协议里声明的
属性或方法，就认为满足协议：

```python
from typing import Protocol

class Priced(Protocol):
    price: float

def total_value(items: list[Priced]) -> float:
    return sum(item.price for item in items)
```

加上 `@runtime_checkable` 后，`isinstance(obj, Priced)` 才能工作；否则 Protocol 主要用于
静态类型检查。

## 5. 类型标注是辅助，不是枷锁

Python 仍然是动态语言。类型标注帮助：
- 人快速理解函数契约；
- 静态工具（mypy、pyright、IDE）提前发现错误；
- 小娜等学习助手更好地解释代码。

但运行时不一定按标注执行，关键校验仍需要显式代码或 `__post_init__`。

## 6. 常见错误

- 在 dataclass 字段里直接写 `items: list[str] = []`，导致所有实例共享同一列表。
- 以为 `frozen=True` 只是“不能改属性”，忽略它同时让实例变得可哈希。
- 把 `Protocol` 当成强制基类去继承；实际上它表达的是“能力”而非“血统”。
- 以为写了类型标注就能在运行时自动阻止类型错误；类型检查主要由静态工具完成。
