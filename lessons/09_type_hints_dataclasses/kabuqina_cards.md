# Kabuqina Cards · Lesson 09 Type Hints and Dataclasses

## Concept Card 1
Q: `@dataclass` 为什么能减少样板代码？
A: 它根据字段声明自动生成 `__init__`、`__repr__`、`__eq__` 等方法，让数据类聚焦语义。

## Concept Card 2
Q: `typing.Protocol` 与 `abc.ABC` / 普通继承有什么区别？
A: Protocol 是结构化子类型：不强制继承，只要对象实现了协议要求的属性/方法就算匹配。

## Code Card 1
Q: 为什么 dataclass 的可变默认值必须用 `field(default_factory=...)`？
A: 类属性在类定义时只求值一次；写 `= []` 会让所有实例共享同一个列表。

## Misconception Card 1
Q: 写了类型标注，Python 运行时就会自动阻止类型错误吗？
A: 不会。类型标注主要是静态检查和文档；运行时验证需要显式代码或 `__post_init__`。

## Tutor Prompt
请像助教一样，先让学生把一个用普通 `class` 和手写 `__init__` 实现的 `Book` 类改写成 `@dataclass`，
再问他：如果要让 `Book` 不可变且能放进 `set` 里，应该加什么参数？
