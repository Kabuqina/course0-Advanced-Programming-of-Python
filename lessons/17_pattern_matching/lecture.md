# Lesson 17 讲义 · 结构化模式匹配（match/case）

> 本课需要 Python 3.10+。

## 1. match/case 不是 switch 的语法糖

很多语言里的 `switch` 是按值比较；Python 的 `match/case` 做的是**结构匹配**：
命中某个分支的同时，把数据内部的字段**解构**到变量里。

```python
def describe_event(event: dict) -> str:
    match event:
        case {"type": "click", "x": x, "y": y}:
            return f"click at ({x}, {y})"
        case {"type": "key", "key": key}:
            return f"key {key}"
        case _:
            return "malformed event"
```

## 2. 映射模式

`{"type": "click", "x": x, "y": y}` 表示：字典至少包含这些键； `"click"` 是字面量匹配，
`x` 和 `y` 是捕获变量。多余的键不影响匹配。

```python
event = {"type": "click", "x": 10, "y": 20, "timestamp": 123}
# 仍会命中第一个 case，x=10, y=20
```

## 3. 序列模式、或模式、守卫

```python
def parse_command(tokens: list[str]) -> str:
    match tokens:
        case []:
            return "empty"
        case ["go", direction]:
            return f"move {direction}"
        case ["take", *items]:
            return f"take {len(items)} item(s)"
        case [single]:
            return f"single command: {single}"
        case _:
            return "unrecognized"
```

- `case 200 | 201 | 204:`：或模式，多个值命中同一分支。
- `case c if 400 <= c < 500:`：守卫（guard），在模式命中后进一步判断。

## 4. 变量捕获 vs 常量比较

case 分支里，**裸变量名是捕获**，不是比较。如果要比较常量，必须写字面量或枚举/类属性：

```python
RED = "red"

def check(c):
    match c:
        case RED:          # 错误：把 RED 的值捕获到变量 RED 里，永远命中
            return "red"
        case "red":        # 正确：与字符串字面量比较
            return "red"
```

## 5. 顺序敏感

match 从上到下匹配，第一个命中的分支立即执行。兜底分支 `case _:` 要放在最后。

## 6. 常见错误

- 把 `case 变量名` 当成“等于这个变量的值”去做比较。
- 把 `case _:` 放在中间，导致后面的分支永远执行不到。
- 以为映射模式要求字典只能有列出的键；其实多余键是被忽略的。
- 在 Python 3.9 或更早环境使用 `match/case`，直接报语法错误。
