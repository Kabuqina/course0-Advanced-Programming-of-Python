import pytest

from course_loader import DATA, load

m = load("03_iterators_generators")


def test_read_ints_first_three():
    assert m.take(m.read_ints(DATA / "numbers.txt"), 3) == [3, 15, 8]


def test_running_max():
    assert list(m.running_max([3, 1, 4, 1, 5, 9, 2])) == [3, 3, 4, 4, 5, 9, 9]


def test_chunk():
    assert list(m.chunk([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]


def test_chunk_rejects_bad_size():
    with pytest.raises(ValueError):
        list(m.chunk([1, 2, 3], 0))


def test_revenue_by_region():
    rev = m.revenue_by_region(DATA / "sales.csv")
    assert set(rev) == {"north", "south", "east", "west"}
    # north: 12*9.90 + 8*24.50 + 7*9.90 + 2*49.00 + 6*24.50 = 629.10
    assert rev["north"] == 629.10
