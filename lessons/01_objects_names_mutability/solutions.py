"""Lesson 01 参考解答：对象、名字与可变性。"""

from __future__ import annotations

import copy
from typing import Any, Dict, List, Optional


def add_grade(grade: int, scores: Optional[List[int]] = None) -> List[int]:
    """追加 grade 到 scores；不传则新建空列表（避免可变默认参数陷阱）。"""
    if scores is None:
        scores = []
    scores.append(grade)
    return scores


def safe_update_config(base: Dict[str, Any], patch: Dict[str, Any]) -> Dict[str, Any]:
    """合并 patch 到 base 的深拷贝上，递归合并嵌套 dict，不污染 base。"""
    result = copy.deepcopy(base)
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = safe_update_config(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result


def independent_copy(data: Any) -> Any:
    """返回与 data 相等但完全独立的深拷贝。"""
    return copy.deepcopy(data)


if __name__ == "__main__":
    print("add_grade(90):", add_grade(90))
    print("add_grade(80):", add_grade(80), "(独立，不共享)")

    base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
    patch = {"db": {"port": 5433}, "debug": True}
    print("merged:", safe_update_config(base, patch))
    print("base 保持不变:", base)
