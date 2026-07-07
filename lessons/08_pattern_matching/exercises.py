"""模块 8 练习：实现下列函数，使对应测试通过（需要 Python 3.10+）。

做完后对照 solutions.py。提示：用 match/case 的映射模式与捕获变量。
"""

from __future__ import annotations

import json  # noqa: F401
import math  # noqa: F401
from pathlib import Path
from typing import Dict, Iterable, List

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def describe_event(event: Dict) -> str:
    """把 UI 事件描述成字符串：

    - {"type":"click","x":X,"y":Y}  -> "click at (X, Y)"
    - {"type":"key","key":K}        -> "key K"
    - {"type":"scroll","dy":D}      -> "scroll up/down |D|"（D>0 为 up）
    - {"type":"resize","width":W,"height":H} -> "resize to WxH"
    - 其它有 type 的                 -> "unknown event: TYPE"
    - 没有 type 的                   -> "malformed event"
    """
    raise NotImplementedError


def count_event_types(events: Iterable[Dict]) -> Dict[str, int]:
    """统计各 type 次数；无 type 字段计入 '_malformed'。"""
    raise NotImplementedError


def load_events(path: str | Path) -> List[Dict]:
    """读取 events.json。"""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def shape_area(shape: Dict) -> float:
    """按 kind 求面积：circle(r) / rect(w,h) / square(side)；未知抛 ValueError。"""
    raise NotImplementedError
