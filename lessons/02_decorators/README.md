# 模块 2 · 装饰器与闭包

## 目标
- 理解闭包：内层函数捕获外层作用域变量
- 掌握装饰器：接收函数、返回函数的高阶函数
- 用 `functools.wraps` 保留被装饰函数的元信息
- 写**带参数**的装饰器（三层结构）

## 要点

`@deco` 等价于 `func = deco(func)`。装饰器常用于横切关注点：计时、缓存、重试、
日志、权限。

```python
import functools

def count_calls(func):
    @functools.wraps(func)          # 保留 __name__/__doc__/签名
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper
```

**带参数的装饰器**再包一层工厂函数：

```python
def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times - 1:
                        raise
        return wrapper
    return decorator
```

> 务必使用 `functools.wraps`，否则 `wrapper` 会覆盖原函数的名字、文档与签名，
> 影响调试与自省。

## 本模块练习（见 `exercises.py`）
1. `memoize`：结果缓存装饰器（相同参数不重复计算）
2. `retry`：失败重试指定次数
3. `status_counts`：解析 `data/access.log`，统计各 HTTP 状态码出现次数

运行示例：`python lessons/02_decorators/examples.py`
