import pytest

from course_loader import load

m = load("04_itertools_pipelines")


def test_fib_sequence():
    assert [m.fib(i) for i in range(8)] == [0, 1, 1, 2, 3, 5, 8, 13]


def test_fib_negative_raises():
    with pytest.raises(ValueError):
        m.fib(-1)


def test_compose_order():
    inc = lambda x: x + 1  # noqa: E731
    dbl = lambda x: x * 2  # noqa: E731
    assert m.compose(inc, dbl)(5) == 11  # inc(dbl(5)) = inc(10) = 11
    assert m.compose(dbl, inc)(5) == 12  # dbl(inc(5)) = dbl(6) = 12


def test_compose_empty_is_identity():
    assert m.compose()(42) == 42


def test_describe_dispatch():
    assert m.describe(42) == "int: 42"
    assert m.describe("abc") == "str of length 3"
    assert m.describe([1, 2]) == "list of 2 items"
    assert m.describe(3.14).startswith("object:")


def test_chunked():
    assert list(m.chunked([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert list(m.chunked([], 3)) == []


def test_chunked_rejects_bad_size():
    with pytest.raises(ValueError):
        list(m.chunked([1, 2], 0))


def test_running_total():
    assert m.running_total([1, 2, 3, 4]) == [1, 3, 6, 10]


def test_group_consecutive():
    assert m.group_consecutive("aaabbc") == [("a", 3), ("b", 2), ("c", 1)]
