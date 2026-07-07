# 模块 7 · functools 与 itertools

## 目标
- 用 `functools.lru_cache` 做记忆化，几行改写指数级递归
- 用 `functools.reduce` 组合函数、聚合序列
- 用 `functools.singledispatch` 按参数类型分派（函数版「重载」）
- 用 `itertools` 惰性处理数据流：`islice` / `accumulate` / `groupby` / `chain`

## 要点

**记忆化**：给纯函数加一行装饰器即可缓存：

```python
import functools

@functools.lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```

**单分派**：按第一个参数的类型选择实现：

```python
@functools.singledispatch
def describe(obj):
    return f"object: {obj!r}"

@describe.register
def _(obj: int):
    return f"int: {obj}"
```

**itertools 惰性组合**（不一次性materialize，省内存）：

```python
import itertools
# 分块：每次取 size 个
chunk = list(itertools.islice(it, size))
# 前缀和
list(itertools.accumulate([1, 2, 3]))   # [1, 3, 6]
# 连续相同值聚合
[(k, len(list(g))) for k, g in itertools.groupby("aabbb")]  # [('a',2),('b',3)]
```

## 本模块练习（见 `exercises.py`）
1. `fib`：`lru_cache` 记忆化斐波那契，`n < 0` 抛 ValueError
2. `compose(*funcs)`：从右到左组合，`compose(f, g)(x) == f(g(x))`
3. `describe`：`singledispatch` 分派 int / str / list，其余走默认
4. `chunked` / `running_total` / `group_consecutive`：itertools 惰性处理

运行示例：`python lessons/07_functools_itertools/examples.py`
