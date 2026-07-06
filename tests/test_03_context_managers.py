import os
from pathlib import Path

import pytest

from course_loader import load

m = load("03_context_managers")


def test_timer_records_elapsed():
    with m.Timer() as t:
        sum(range(10000))
    assert t.elapsed >= 0.0


def test_suppress_errors_swallows_listed():
    with m.suppress_errors(ValueError):
        int("not a number")  # should not raise out of the block


def test_suppress_errors_reraises_others():
    with pytest.raises(KeyError):
        with m.suppress_errors(ValueError):
            raise KeyError("x")


def test_working_directory_restores(tmp_path):
    before = os.getcwd()
    with m.working_directory(tmp_path):
        assert Path(os.getcwd()).resolve() == Path(tmp_path).resolve()
    assert os.getcwd() == before


def test_atomic_write_commits(tmp_path):
    target = tmp_path / "out.txt"
    with m.atomic_write(target) as f:
        f.write("hello")
    assert target.read_text(encoding="utf-8") == "hello"
    assert not (tmp_path / "out.txt.tmp").exists()


def test_atomic_write_cleans_up_on_error(tmp_path):
    target = tmp_path / "out.txt"
    with pytest.raises(RuntimeError):
        with m.atomic_write(target) as f:
            f.write("partial")
            raise RuntimeError("boom")
    assert not target.exists()
    assert not (tmp_path / "out.txt.tmp").exists()
