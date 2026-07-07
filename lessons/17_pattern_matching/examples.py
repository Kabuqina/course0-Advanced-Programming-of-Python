"""Lesson 17（选讲）可运行示例：match/case 的多种模式。

直接运行：``python lessons/17_pattern_matching/examples.py``
需要 Python 3.10+。
"""

from __future__ import annotations

from typing import Any


def http_status_text(code: int) -> str:
    """值模式 + 或模式（|）+ 守卫（if）。"""
    match code:
        case 200 | 201 | 204:
            return "success"
        case 301 | 302:
            return "redirect"
        case c if 400 <= c < 500:
            return "client error"
        case c if 500 <= c < 600:
            return "server error"
        case _:
            return "unknown"


def parse_command(tokens: list[str]) -> str:
    """序列模式：按列表结构解构。"""
    match tokens:
        case []:
            return "empty"
        case ["go", direction]:
            return f"move {direction}"
        case ["take", *items]:
            return f"take {len(items)} item(s): {', '.join(items)}"
        case [single]:
            return f"single command: {single}"
        case _:
            return "unrecognized"


def summarize(value: Any) -> str:
    """类型 + 结构混合匹配。"""
    match value:
        case {"name": str(name), "age": int(age)}:
            return f"{name} is {age}"
        case [x, y]:
            return f"pair ({x}, {y})"
        case str() as s:
            return f"string: {s}"
        case _:
            return "other"


def main() -> None:
    for code in (200, 301, 404, 503, 999):
        print(f"  {code}: {http_status_text(code)}")
    print(parse_command(["go", "north"]))
    print(parse_command(["take", "sword", "shield"]))
    print(parse_command([]))
    print(summarize({"name": "Alice", "age": 30}))
    print(summarize([1, 2]))
    print(summarize("hello"))


if __name__ == "__main__":
    main()
