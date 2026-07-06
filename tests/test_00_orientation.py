from course_loader import load

m = load("00_orientation")


def test_greet():
    assert m.greet("Kabuqina") == "Hello, Kabuqina! Welcome to Course0."


def test_python_at_least_true():
    assert m.python_at_least(3, 10) is True


def test_python_at_least_future_false():
    assert m.python_at_least(99, 0) is False


def test_environment_report_keys():
    report = m.environment_report()
    assert {"python_version", "executable", "cwd"} <= set(report)
    assert all(isinstance(v, str) for v in report.values())
