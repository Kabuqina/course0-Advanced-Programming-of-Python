"""Lesson 01 练习：实现下列函数，使 tests/test_01_objects_names_mutability.py 通过。

重点：不要让可变对象在调用间被共享或污染。做完对照 solutions.py。
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


def add_grade(grade: int, scores: Optional[List[int]] = None) -> List[int]:
    """把 grade 追加到 scores 并返回。

    - 不传 scores 时每次都应从**新的空列表**开始（修复可变默认参数陷阱）。
    - 传入 scores 时，就地追加并返回同一个列表。
    """
    raise NotImplementedError


def safe_update_config(base: Dict[str, Any], patch: Dict[str, Any]) -> Dict[str, Any]:
    """返回 base 合并 patch 后的**新** dict，且不修改 base（含嵌套 dict）。

    - 嵌套 dict 应递归合并。
    - 合并结果与 base 不能共享任何可变子对象。
    """
    raise NotImplementedError


def independent_copy(data: Any) -> Any:
    """返回与 data 相等但完全独立的深拷贝（嵌套子对象也不共享）。"""
    raise NotImplementedError
