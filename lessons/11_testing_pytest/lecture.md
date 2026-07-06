# Lesson 11 讲义 · 测试、回归与可验证代码

## 1. 为什么测试
测试把“主观相信”变成“可重复验证”。它还是一张安全网：重构或加功能后，一键确认
没有破坏既有行为（回归）。好的测试也是最诚实的文档——它写明了函数在各种输入下的预期。

## 2. pytest 基础
- 文件名 `test_*.py`，函数名 `test_*`，用普通 `assert`。
- 运行：`pytest`（本仓库 `pyproject.toml` 已配置 `testpaths=["tests"]`）。
- 失败时 pytest 会展开 `assert` 两侧的值，定位很直观。

```python
def test_running_total_basic():
    assert running_total([1, 2, 3]) == [1, 3, 6]
```

## 3. 参数化：一份逻辑，多组数据
```python
import pytest

@pytest.mark.parametrize("text, expected", [
    ("true", True), ("Yes", True), ("1", True),
    ("false", False), ("no", False), ("0", False),
])
def test_parse_bool(text, expected):
    assert parse_bool(text) is expected
```
避免复制粘贴多个几乎相同的测试；新增用例只加一行数据。

## 4. 异常路径：`pytest.raises`
```python
def test_parse_bool_rejects_garbage():
    with pytest.raises(ValueError):
        parse_bool("maybe")
```
不仅测“对的情况”，更要测“错的情况”——错误处理往往是 bug 高发区。

## 5. fixture 与 `tmp_path`
fixture 提供测试所需的“环境/数据”，由 pytest 注入。内置 `tmp_path` 给每个测试一个
独立的临时目录，天然隔离、自动清理：
```python
def test_word_count(tmp_path):
    f = tmp_path / "sample.txt"
    f.write_text("a a b\n", encoding="utf-8")
    assert word_count(f) == {"a": 2, "b": 1}
```
也可以用 `@pytest.fixture` 定义自己的：
```python
@pytest.fixture
def sample_numbers():
    return [3, 1, 4, 1, 5]
```

## 6. 回归测试的节奏
1. 复现 bug：写一个**当前会失败**的测试。
2. 修实现，直到测试变绿。
3. 保留该测试，防止同样的 bug 再回来。

## 7. 常见错误
- 只测 happy path，不测边界（空输入、非法输入、超大输入）。
- 一个测试断言太多、职责不清，失败了看不出是哪出问题。
- 测试之间共享可变状态、依赖执行顺序，导致偶发失败。
- 用真实文件/网络而非 `tmp_path`/mock，测试变慢且不稳定。
