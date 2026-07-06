"""模块 3 参考解答：上下文管理器。"""

from __future__ import annotations

import contextlib
import os
import time
from pathlib import Path
from typing import Iterator

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


class Timer:
    """上下文管理器：记录 with 块的耗时到 .elapsed（秒）。"""

    def __enter__(self) -> "Timer":
        self._start = time.perf_counter()
        self.elapsed = 0.0
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        self.elapsed = time.perf_counter() - self._start
        return False  # 不吞异常


@contextlib.contextmanager
def working_directory(path: str | Path) -> Iterator[Path]:
    """临时切换工作目录，退出时恢复。"""
    previous = os.getcwd()
    os.chdir(path)
    try:
        yield Path(path)
    finally:
        os.chdir(previous)


@contextlib.contextmanager
def suppress_errors(*exceptions: type[BaseException]) -> Iterator[None]:
    """抑制指定异常类型（未指定则不抑制任何异常）。"""
    try:
        yield
    except exceptions:
        pass


@contextlib.contextmanager
def opened_lines(path: str | Path) -> Iterator[Iterator[str]]:
    """产出去空白的非空行迭代器，确保文件最终关闭。"""
    f = open(path, encoding="utf-8")
    try:
        yield (line.strip() for line in f if line.strip())
    finally:
        f.close()


@contextlib.contextmanager
def atomic_write(path: str | Path, encoding: str = "utf-8") -> Iterator:
    """原子写：先写临时文件，成功后替换目标；失败则清理临时文件。"""
    path = Path(path)
    tmp = path.with_name(path.name + ".tmp")
    handle = open(tmp, "w", encoding=encoding)
    try:
        yield handle
        handle.close()
        os.replace(tmp, path)  # 原子替换
    except BaseException:
        handle.close()
        if tmp.exists():
            tmp.unlink()
        raise


if __name__ == "__main__":
    with Timer() as t:
        sum(range(100000))
    print(f"elapsed: {t.elapsed*1000:.2f} ms")

    with opened_lines(DATA_DIR / "numbers.txt") as lines:
        print("first 3 numbers:", [next(lines) for _ in range(3)])
