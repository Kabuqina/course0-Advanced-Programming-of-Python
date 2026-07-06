# 模块 3 · 上下文管理器

## 目标
- 用 `with` 保证资源被**确定性释放**，即使发生异常
- 实现 `__enter__` / `__exit__` 协议
- 用 `contextlib.contextmanager` 以生成器方式简化写法
- 掌握常见模式：计时、切换工作目录、原子写文件、抑制异常

## 要点

`with cm as x:` 进入时调用 `cm.__enter__()`（其返回值绑定给 `x`），离开时调用
`cm.__exit__(exc_type, exc, tb)`——无论正常结束还是异常。`__exit__` 返回真值表示
异常已被处理、不再向外传播。

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        import time
        self.elapsed = time.perf_counter() - self.start
        return False          # 不吞异常
```

**生成器写法**：`yield` 之前相当于 `__enter__`，`finally` 部分相当于 `__exit__`：

```python
import contextlib, os

@contextlib.contextmanager
def working_directory(path):
    prev = os.getcwd()
    os.chdir(path)
    try:
        yield path
    finally:
        os.chdir(prev)         # 一定会执行
```

**原子写**是重要工程模式：先写临时文件，成功后再 `os.replace` 覆盖目标，避免写到
一半留下损坏文件。

## 本模块练习（见 `exercises.py`）
1. `Timer`：上下文管理器，退出后 `.elapsed` 为耗时
2. `suppress_errors(*excs)`：抑制指定异常
3. `atomic_write(path)`：原子写入（临时文件 + 替换，失败清理）

运行示例：`python lessons/03_context_managers/examples.py`
