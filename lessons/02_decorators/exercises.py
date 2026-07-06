"""模块 2 练习：实现下列装饰器/函数，使对应测试通过。

记得用 functools.wraps 保留元信息。做完后对照 solutions.py。
"""

from __future__ import annotations

import functools  # noqa: F401  (练习中应会用到)
import re
from pathlib import Path
from typing import Callable, Dict, Optional

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

_LOG_RE = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) [^"]+" (?P<status>\d+) (?P<bytes>\d+)$'
)


def memoize(func: Callable) -> Callable:
    """按位置参数缓存结果（参数可哈希）。相同参数不应重复调用 func。

    提示：用一个 dict 做缓存；可把它暴露在 wrapper.cache 上便于观察。
    """
    raise NotImplementedError


def retry(times: int = 3, exceptions=(Exception,)) -> Callable:
    """带参装饰器：捕获 exceptions 并重试，最多 times 次；最后仍失败则抛出。

    times < 1 抛 ValueError。
    """
    raise NotImplementedError


def parse_log_line(line: str) -> Optional[Dict[str, object]]:
    """解析一行访问日志为 {ip, method, path, status:int, bytes:int}；不匹配返回 None。"""
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
    """统计访问日志中各 HTTP 状态码出现次数（用 parse_log_line）。"""
    raise NotImplementedError
