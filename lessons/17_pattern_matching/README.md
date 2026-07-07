# Lesson 17（选讲）· 结构化模式匹配（match/case）

> 需要 Python 3.10+。
> 迁移自旧 `08_pattern_matching`。模式匹配不在 `course_structure.md` 的 17 课主线中，
> 作为**选讲/附加**内容保留于编号 17。

## 目标
- 用 `match/case` 按**结构**解构数据，而非一串 `if/elif`
- 掌握映射模式 `{"key": value}`、捕获变量、通配 `_`
- 理解「匹配即解构」：命中分支的同时把子字段绑定到变量

## 要点

`match` 对值做结构匹配，命中即解构：

```python
def describe_event(event: dict) -> str:
    match event:
        case {"type": "click", "x": x, "y": y}:      # 映射模式 + 捕获
            return f"click at ({x}, {y})"
        case {"type": "key", "key": key}:
            return f"key {key}"
        case {"type": t}:                            # 只要有 type 字段
            return f"unknown event: {t}"
        case _:                                      # 兜底
            return "malformed event"
```

要点：

- 映射模式只要求「至少包含这些键」，多余的键不影响匹配。
- `case` 里的裸变量是**捕获**（绑定），不是比较；要比较常量得写字面量或 `case Color.RED`。
- 顺序敏感：从上到下第一个命中的分支生效，把兜底 `case _` 放最后。

## 本模块练习（见 `exercises.py`）
1. `describe_event`：匹配 click / key / scroll / resize，其余归为 unknown / malformed
2. `count_event_types`：统计 `data/events.json` 里各 `type` 出现次数
3. `shape_area`：按 `kind` 匹配 circle / rect / square 求面积，未知形状抛 ValueError

运行示例：`python lessons/17_pattern_matching/examples.py`
