"""模块 8 参考解答：结构化模式匹配（match/case，Python 3.10+）。"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, Iterable, List

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def describe_event(event: Dict) -> str:
    """把一个 UI 事件字典描述成人类可读字符串。"""
    match event:
        case {"type": "click", "x": x, "y": y}:
            return f"click at ({x}, {y})"
        case {"type": "key", "key": key}:
            return f"key {key}"
        case {"type": "scroll", "dy": dy}:
            direction = "up" if dy > 0 else "down"
            return f"scroll {direction} {abs(dy)}"
        case {"type": "resize", "width": w, "height": h}:
            return f"resize to {w}x{h}"
        case {"type": t}:
            return f"unknown event: {t}"
        case _:
            return "malformed event"


def count_event_types(events: Iterable[Dict]) -> Dict[str, int]:
    """统计各事件 type 出现次数；无 type 字段计入 '_malformed'。"""
    counts: Dict[str, int] = {}
    for event in events:
        match event:
            case {"type": t}:
                counts[t] = counts.get(t, 0) + 1
            case _:
                counts["_malformed"] = counts.get("_malformed", 0) + 1
    return counts


def load_events(path: str | Path) -> List[Dict]:
    """读取 events.json。"""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def shape_area(shape: Dict) -> float:
    """按 kind 匹配求面积；未知形状抛 ValueError。"""
    match shape:
        case {"kind": "circle", "r": r}:
            return math.pi * r * r
        case {"kind": "rect", "w": w, "h": h}:
            return float(w * h)
        case {"kind": "square", "side": s}:
            return float(s * s)
        case _:
            raise ValueError(f"unknown shape: {shape}")


if __name__ == "__main__":
    events = load_events(DATA_DIR / "events.json")
    for event in events:
        print(" ", describe_event(event))
    print("counts:", count_event_types(events))
    print("rect area:", shape_area({"kind": "rect", "w": 3, "h": 4}))
