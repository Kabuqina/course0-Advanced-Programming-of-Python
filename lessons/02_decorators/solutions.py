"""模块 2 参考解答：装饰器与闭包。"""

from __future__ import annotations

import functools
import re
from pathlib import Path
from typing import Callable, Dict, Optional

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

_LOG_RE = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) [^"]+" (?P<status>\d+) (?P<bytes>\d+)$'
)


def count_calls(func: Callable) -> Callable:
    """统计函数被调用次数，暴露在 wrapper.calls 上。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def memoize(func: Callable) -> Callable:
    """按位置参数缓存结果（要求参数可哈希）。"""
    cache: Dict[tuple, object] = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.cache = cache
    return wrapper


def retry(times: int = 3, exceptions=(Exception,)) -> Callable:
    """带参装饰器：捕获指定异常并重试，最后一次仍失败则抛出。"""
    if times < 1:
        raise ValueError("times must be >= 1")

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc: Optional[BaseException] = None
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:  # noqa: PERF203
                    last_exc = exc
            raise last_exc  # type: ignore[misc]

        return wrapper

    return decorator


def parse_log_line(line: str) -> Optional[Dict[str, object]]:
    """解析一行访问日志为字典；无法匹配返回 None。"""
    match = _LOG_RE.match(line.strip())
    if not match:
        return None
    data = match.groupdict()
    return {
        "ip": data["ip"],
        "method": data["method"],
        "path": data["path"],
        "status": int(data["status"]),
        "bytes": int(data["bytes"]),
    }


def status_counts(path: str | Path) -> Dict[int, int]:
    """统计访问日志中各 HTTP 状态码出现次数。"""
    counts: Dict[int, int] = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            record = parse_log_line(line)
            if record is None:
                continue
            status = record["status"]
            counts[status] = counts.get(status, 0) + 1
    return counts


if __name__ == "__main__":
    @count_calls
    def greet(name):
        return f"hi {name}"

    greet("a"); greet("b")
    print("calls:", greet.calls)
    print("status_counts:", status_counts(DATA_DIR / "access.log"))
