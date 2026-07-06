# Lesson 06 讲义 · 上下文管理器与资源安全

## 1. 为什么需要 `with`
资源（文件、锁、连接、临时状态）必须**确定性释放**，否则会泄漏或留下脏状态。
`try/finally` 能做到，但每次都写很啰嗦。`with` 把“获取 + 释放”封装成一个对象。

```python
with open("f.txt") as f:
    data = f.read()
# 到这里文件一定已关闭，哪怕 read() 抛异常
```

## 2. 协议：`__enter__` / `__exit__`
```python
class Guard:
    def __enter__(self):
        # 获取资源；返回值绑定到 as 后的名字
        return self
    def __exit__(self, exc_type, exc, tb):
        # 释放资源；无论正常/异常都会调用
        return False   # 返回 True 表示“吞掉异常”，False 让异常继续传播
```
`__exit__` 的三个参数：无异常时都是 `None`；有异常时分别是异常类型、实例、traceback。

## 3. 生成器写法：`contextlib.contextmanager`
用一个 `yield` 把“进入/退出”写在一起，更短：
```python
import contextlib, time

@contextlib.contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield                       # yield 之前 = __enter__
    finally:
        print(time.perf_counter() - start)   # finally = __exit__
```
把清理放在 `finally`，保证异常时也会执行。

## 4. 工程模式：原子写
避免“写到一半崩溃留下半个损坏文件”：先写临时文件，成功后 `os.replace` 原子替换。
```python
@contextlib.contextmanager
def atomic_write(path):
    tmp = path.with_name(path.name + ".tmp")
    f = open(tmp, "w", encoding="utf-8")
    try:
        yield f
        f.close()
        os.replace(tmp, path)       # 原子替换
    except BaseException:
        f.close()
        if tmp.exists():
            tmp.unlink()            # 失败清理，目标保持原样
        raise
```

## 5. 相关工具
- `contextlib.suppress(*excs)`：抑制指定异常。
- `contextlib.ExitStack`：动态管理数量不定的上下文（如一次打开多个文件）。

## 6. 常见错误
- `__exit__` 误返回 `True`，无意中吞掉了异常，掩盖 bug。
- 把清理逻辑写在 `yield` 之后但不放进 `finally`，异常时清理被跳过。
- 原子写失败后忘记删除临时文件，留下 `.tmp` 垃圾。
- 以为 `with` 会“重试”——它只负责获取/释放，不负责错误恢复。
