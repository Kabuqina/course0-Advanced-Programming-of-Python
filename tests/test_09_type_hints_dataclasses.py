import pytest

from course_loader import DATA, load

m = load("09_type_hints_dataclasses")


def test_money_add_and_str():
    a = m.Money(1050)  # 10.50 CNY
    b = m.Money(200)
    assert a.plus(b) == m.Money(1250)
    assert str(a) == "10.50 CNY"


def test_money_is_frozen():
    a = m.Money(100)
    with pytest.raises(Exception):
        a.cents = 0  # frozen -> FrozenInstanceError


def test_money_validates_negative_and_currency():
    with pytest.raises(ValueError):
        m.Money(-1)
    with pytest.raises(ValueError):
        m.Money(100, "YENN")


def test_money_rejects_cross_currency_add():
    with pytest.raises(ValueError):
        m.Money(100, "CNY").plus(m.Money(100, "USD"))


def test_load_employees():
    emps = m.load_employees(DATA / "employees.csv")
    assert len(emps) == 8
    assert emps[0].name == "Alice Chen"
    assert emps[0].salary == 95000


def test_by_department_counts():
    emps = m.load_employees(DATA / "employees.csv")
    counts = {k: len(v) for k, v in m.by_department(emps).items()}
    assert counts == {"Engineering": 4, "Design": 2, "Marketing": 2}


def test_highest_paid():
    emps = m.load_employees(DATA / "employees.csv")
    assert m.highest_paid(emps).name == "David Zhao"


def test_highest_paid_empty_raises():
    with pytest.raises(ValueError):
        m.highest_paid([])


def test_total_value_protocol():
    from dataclasses import dataclass

    @dataclass
    class Item:
        price: float

    assert m.total_value([Item(1.5), Item(2.5), Item(3.0)]) == 7.0
