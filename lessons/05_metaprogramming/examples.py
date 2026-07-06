"""模块 5 可运行示例：描述符校验、property、__init_subclass__ 注册。

直接运行：``python lessons/05_metaprogramming/examples.py``
"""

from __future__ import annotations


class Ranged:
    """限定取值范围的描述符。"""

    def __init__(self, low, high):
        self.low, self.high = low, high

    def __set_name__(self, owner, name):
        self.private = "_" + name
        self.name = name

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        return getattr(obj, self.private)

    def __set__(self, obj, value):
        if not (self.low <= value <= self.high):
            raise ValueError(f"{self.name} must be in [{self.low}, {self.high}]")
        setattr(obj, self.private, value)


class Thermostat:
    celsius = Ranged(-40, 125)

    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):           # property 本身也是描述符
        return self.celsius * 9 / 5 + 32


class Shape:
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Shape.registry[cls.__name__.lower()] = cls


def main() -> None:
    t = Thermostat(25)
    print("25C ->", t.fahrenheit, "F")
    try:
        Thermostat(999)
    except ValueError as exc:
        print("rejected:", exc)

    class Circle(Shape):
        pass

    class Square(Shape):
        pass

    print("registered shapes:", sorted(Shape.registry))


if __name__ == "__main__":
    main()
