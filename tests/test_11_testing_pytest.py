"""本文件既是 Lesson 11 的测试，也是“如何写 pytest”的教学样例：
展示 parametrize / pytest.raises / 自定义 fixture / 内置 tmp_path 四种用法。
"""

import pytest

from course_loader import load

m = load("11_testing_pytest")


# --- 参数化：一份逻辑覆盖多组输入 ---
@pytest.mark.parametrize(
    "text, expected",
    [
        ("true", True),
        ("Yes", True),
        (" 1 ", True),
        ("ON", True),
        ("false", False),
        ("no", False),
        ("0", False),
        ("Off", False),
    ],
)
def test_parse_bool(text, expected):
    assert m.parse_bool(text) is expected


# --- 异常路径：pytest.raises ---
@pytest.mark.parametrize("bad", ["maybe", "", "2", "truue"])
def test_parse_bool_rejects_garbage(bad):
    with pytest.raises(ValueError):
        m.parse_bool(bad)


# --- 自定义 fixture ---
@pytest.fixture
def sample_numbers():
    return [3, 1, 4, 1, 5]


def test_running_total_with_fixture(sample_numbers):
    assert m.running_total(sample_numbers) == [3, 4, 8, 9, 14]


def test_running_total_empty():
    assert m.running_total([]) == []


# --- 内置 tmp_path fixture：隔离的临时文件 ---
def test_word_count(tmp_path):
    f = tmp_path / "sample.txt"
    f.write_text("apple apple banana\ncarrot apple\n", encoding="utf-8")
    assert m.word_count(f) == {"apple": 3, "banana": 1, "carrot": 1}


def test_word_count_empty_file(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("", encoding="utf-8")
    assert m.word_count(f) == {}
