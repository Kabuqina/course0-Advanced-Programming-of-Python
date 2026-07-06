"""Lesson 11 可运行示例：被测函数的直接演示（不依赖 pytest）。

真正的“教学样例”是 tests/test_11_testing_pytest.py，它展示 parametrize / fixture /
raises / tmp_path。这里只是把被测函数跑一遍，直观感受它们的行为。

直接运行：``python lessons/11_testing_pytest/examples.py``
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from solutions import parse_bool, running_total, word_count  # noqa: E402  type: ignore


def main() -> None:
    print("parse_bool('Yes') =", parse_bool("Yes"))
    print("parse_bool('0')   =", parse_bool("0"))
    print("running_total([1,2,3,4]) =", running_total([1, 2, 3, 4]))

    tmp = Path(__file__).resolve().parent / "_demo_words.txt"
    tmp.write_text("apple apple banana\n", encoding="utf-8")
    try:
        print("word_count(demo) =", word_count(tmp))
    finally:
        tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
