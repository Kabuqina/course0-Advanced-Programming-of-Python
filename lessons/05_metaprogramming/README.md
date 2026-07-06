# 模块 5 · 元编程

## 目标
- 用**描述符**拦截属性的读写，实现类型/取值校验
- 掌握 `__set_name__` 自动获知属性名
- 理解 `property` 本质是描述符
- 用 `__init_subclass__` 做子类**自动注册**（多数场景可替代元类）

## 要点

**描述符**是实现了 `__get__` / `__set__` / `__delete__` 之一的对象，放在类属性上即可
拦截实例的属性访问。方法、`property`、`classmethod` 都是描述符。

```python
class Positive:
    def __set_name__(self, owner, name):   # 自动得到属性名
        self.private = "_" + name
        self.name = name
    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        return getattr(obj, self.private)
    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        setattr(obj, self.private, value)

class Account:
    balance = Positive()
```

**`__init_subclass__`** 在**定义子类**时被父类调用，是做插件/注册表的轻量手段，
比自定义元类更简单：

```python
class Plugin:
    registry = {}
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registry[cls.__name__] = cls
```

> 元类（`type` 的子类）是“类的类”，能定制类的创建过程；但它是最后手段——
> 先考虑描述符、类装饰器、`__init_subclass__`。

## 本模块练习（见 `exercises.py`）
1. `Typed(expected_type)`：类型校验描述符
2. `Positive`：正数校验描述符
3. `Plugin.__init_subclass__`：子类自动注册到 `Plugin.registry`

（`Book` 用上述描述符做校验；`make_books` 从 `data/books.json` 构造并校验。）

运行示例：`python lessons/05_metaprogramming/examples.py`
