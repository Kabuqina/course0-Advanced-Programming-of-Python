# Lesson 03 讲义 · 迭代器与生成器

## 1. `for` 背后发生了什么
`for x in obj:` 实际做了三步：`it = iter(obj)`（调用 `obj.__iter__()`）拿到迭代器，
反复 `next(it)`（调用 `it.__next__()`）取值，直到抛出 `StopIteration` 结束。

- **iterable（可迭代对象）**：实现 `__iter__`，能被 `for`/`list()` 遍历，如 list、str、文件。
- **iterator（迭代器）**：实现 `__next__`（且 `__iter__` 返回自身），保存“迭代到哪了”的状态。

```python
class Countdown:
    def __init__(self, n): self.n = n
    def __iter__(self): return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1
```

## 2. 生成器：写迭代器的捷径
含 `yield` 的函数就是生成器函数。调用它**不执行函数体**，只返回一个生成器对象；
每次 `next()` 才执行到下一个 `yield` 并暂停，保留局部状态。

```python
def read_ints(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield int(line)     # 一次只在内存里保留一行
```
生成器表达式 `(expr for x in it if cond)` 是同样惰性的紧凑写法。

## 3. 惰性管道
把多个生成器串联，数据像流水一样按需流过，中间不物化整份列表：
```python
nums    = read_ints("data/numbers.txt")
evens   = (n for n in nums if n % 2 == 0)
squared = (n * n for n in evens)     # 到这里还没读文件
total   = sum(squared)               # 真正驱动消费在这一步
```

## 4. `yield from`
把迭代委托给子可迭代对象，常用于展开嵌套：
```python
def flatten(nested):
    for sub in nested:
        yield from sub
```

## 5. 常见错误
- **生成器只能消费一次**：遍历完就空了，再 `for` 得不到任何值。需要多次遍历就存成 list，
  或每次重新调用生成器函数。
- **过早 `list()`**：`list(read_ints(path))` 把整份数据读进内存，抵消了惰性的意义。
- **忘记 `StopIteration`**：手写迭代器时没有终止条件会无限循环。
- **对无限生成器直接 `list()`**：会挂死；应配合 `itertools.islice` 或提前 break。
