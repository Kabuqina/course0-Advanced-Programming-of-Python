# Lesson 05 讲义 · 装饰器与横切关注点

## 1. 从闭包说起
函数是一等对象：可传递、返回、存入容器。闭包是**记住了外层变量**的内层函数：
```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor      # 捕获外层 factor
    return multiply
triple = make_multiplier(3)
triple(5)   # 15
```

## 2. 装饰器的本质
`@deco` 只是语法糖：
```python
@deco
def f(): ...
# 等价于
def f(): ...
f = deco(f)
```
装饰器接收一个函数、返回一个（通常包了一层的）函数，用来在**不改业务代码**的前提下
增加计时、缓存、重试、日志等能力（横切关注点）。

```python
import functools

def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {(time.perf_counter()-start)*1000:.2f} ms")
        return result
    return wrapper
```

## 3. `functools.wraps` 为什么重要
不加 `wraps`，`wrapper` 会顶替原函数的 `__name__`、`__doc__`、`__wrapped__` 等元信息，
调试时看到的全是 `wrapper`，文档工具、自省、日志都会失真。`@functools.wraps(func)`
把这些元信息复制到 wrapper 上。

## 4. 带参数的装饰器 = 三层
需要给装饰器传参时，最外层是“装饰器工厂”，它返回真正的装饰器：
```python
def retry(times, exceptions=(Exception,)):   # ① 工厂：吃参数
    def decorator(func):                      # ② 装饰器：吃函数
        @functools.wraps(func)
        def wrapper(*args, **kwargs):         # ③ wrapper：吃调用
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == times - 1:
                        raise
        return wrapper
    return decorator
```

## 5. 装饰器顺序
```python
@timed
@repeat(3)
def roll(): ...
```
自下而上应用：`roll = timed(repeat(3)(roll))`。最靠近函数的先包，最外层最后执行进入、
最先执行返回。

## 6. 常见错误
- 忘记 `functools.wraps`，破坏名字/文档/自省。
- 带参装饰器少写一层，导致 `@retry` 而非 `@retry(times=3)` 时行为错乱。
- 在 wrapper 里忘记 `return func(...)` 的返回值，函数“悄悄”变成返回 None。
- 用可变对象做缓存却不考虑参数不可哈希的情况。
