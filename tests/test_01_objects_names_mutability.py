from course_loader import load

m = load("01_objects_names_mutability")


def test_add_grade_no_shared_default():
    a = m.add_grade(90)
    b = m.add_grade(80)
    assert a == [90]
    assert b == [80]  # 不是 [90, 80]：没有共享的可变默认值


def test_add_grade_appends_to_given():
    scores = [70]
    out = m.add_grade(85, scores)
    assert out is scores
    assert scores == [70, 85]


def test_safe_update_config_merges_nested():
    base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
    patch = {"db": {"port": 5433}, "debug": True}
    merged = m.safe_update_config(base, patch)
    assert merged == {"db": {"host": "localhost", "port": 5433}, "debug": True}


def test_safe_update_config_does_not_mutate_base():
    base = {"db": {"host": "localhost", "port": 5432}}
    patch = {"db": {"port": 5433}}
    merged = m.safe_update_config(base, patch)
    assert base == {"db": {"host": "localhost", "port": 5432}}
    assert base["db"] is not merged["db"]


def test_independent_copy_equal_but_distinct():
    data = {"nums": [1, [2, 3]]}
    dup = m.independent_copy(data)
    assert dup == data
    assert dup is not data
    assert dup["nums"] is not data["nums"]
    assert dup["nums"][1] is not data["nums"][1]
