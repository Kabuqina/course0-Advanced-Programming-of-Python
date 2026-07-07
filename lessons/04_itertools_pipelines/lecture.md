# Lesson 04 讲义 · itertools 与函数式管道

## 1. 函数式管道思维

复杂的数据处理可以拆成若干**小、纯、可复用**的步骤，再像拼水管一样串起来：
读取 → 清洗 → 转换 → 聚合。每个步骤只关心一件事，测试和复用都更容易。

```python
# 一个最小管道：先过滤再映射再求和
from functools import reduce
result = sum(map(len, filter(lambda w: w.startswith("a"), words)))
```

## 2. `functools.lru_cache`：记忆化

纯函数（同样输入一定同样输出）的结果可以被缓存，避免重复计算。

```python
import functools

@functools.lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

`maxsize=None` 表示不限容量；生产环境通常设一个合理上限。缓存以参数为键，
所以**被缓存的参数必须可哈希**。

## 3. `functools.partial`：固定参数

把部分参数先绑好，产生一个“更专门”的新函数：

```python
def power(base: float, exp: float) -> float:
    return base ** exp

square = functools.partial(power, exp=2)
cube = functools.partial(power, exp=3)
```

## 4. `functools.singledispatch`：按类型分派

类似函数级别的“重载”，根据**第一个参数的类型**选择实现：

```python
@functools.singledispatch
def describe(obj):
    return f"object: {obj!r}"

@describe.register
def _(obj: int):
    return f"int: {obj}"

@describe.register
def _(obj: str):
    return f"str of length {len(obj)}"
```

注意：`bool` 要在 `int` 之前注册，否则 `True` 会命中 `int` 分支。

## 5. `functools.reduce` 与函数组合

`reduce` 把二元函数累积应用到序列上，`compose` 则是把函数从右到左串起来：

```python
def compose(*funcs):
    def composed(x):
        return functools.reduce(lambda acc, fn: fn(acc), reversed(funcs), x)
    return composed

# compose(f, g)(x) == f(g(x))
```

## 6. `itertools` 惰性工具

itertools 的核心价值是**惰性**：不一次性把所有数据放进内存。

- `islice(it, n)`：从迭代器取前 n 个，返回新的迭代器。
- `accumulate(numbers)`：前缀和 / 累积。
- `groupby(sorted(items), key=...)`：把**连续相同**的元素分组；通常要先排序。
- `chain(a, b, c)`：把多个可迭代对象顺序串起来。

```python
import itertools

# 分块读取
it = iter(range(10))
chunk = list(itertools.islice(it, 3))   # [0, 1, 2]

# 前缀和
list(itertools.accumulate([1, 2, 3, 4]))  # [1, 3, 6, 10]

# 按首字母分组（记得先排序）
words = ["apple", "avocado", "banana", "blueberry"]
for initial, group in itertools.groupby(sorted(words), key=lambda w: w[0]):
    print(initial, list(group))
```

## 7. 常见错误

- 把 `groupby` 当 SQL 的 `GROUP BY` 用，忘记先 `sorted` 或按 key 排序，导致非连续项没有被合并。
- 用 `lru_cache` 缓存参数包含可变对象（如 `list`），触发 `TypeError: unhashable type`。
- `compose(f, g)` 的方向搞反：`compose(f, g)(x)` 应该是 `f(g(x))`。
- `partial(power, 2)` 与 `partial(power, exp=2)` 效果不同，绑定错位置会得到奇怪结果。
