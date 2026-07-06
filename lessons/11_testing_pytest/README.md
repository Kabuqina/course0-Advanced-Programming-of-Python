# Lesson 11 · 测试与 pytest

## 目标
- 把“我觉得能跑”变成“我能证明它在这些场景下是对的”。
- 掌握 pytest 基本要素：`assert`、参数化、fixture、临时目录、异常测试。
- 理解回归测试：先写一个能复现 bug 的失败测试，再修复实现。

## 要点

pytest 用普通 `assert` 断言，失败时给出丰富的对比信息。测试函数以 `test_` 开头，
自动被发现。

```python
def test_parse_bool_true():
    assert parse_bool("yes") is True
```

**参数化**用一组输入覆盖多个场景：

```python
import pytest

@pytest.mark.parametrize("text, expected", [("1", True), ("0", False)])
def test_parse_bool(text, expected):
    assert parse_bool(text) is expected
```

**异常测试**用 `pytest.raises`；**临时文件**用内置 `tmp_path` fixture。

## 本模块被测函数（见 `exercises.py` / `solutions.py`）
1. `parse_bool(s)`：把字符串解析为布尔值，非法输入抛 `ValueError`。
2. `running_total(nums)`：产出累计和列表。
3. `word_count(path)`：统计文本文件里每个词出现次数。

> 学习方式：先读 `tests/test_11_testing_pytest.py`（它就是教学样例，展示 parametrize /
> fixture / raises / tmp_path 四种用法），再在 `exercises.py` 里实现让它变绿。

运行示例：`python lessons/11_testing_pytest/examples.py`
做完练习后：`pytest tests/test_11_testing_pytest.py`
