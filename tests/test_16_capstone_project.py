from course_loader import load

m = load("16_capstone_project")


def _make_lesson(path, files):
    path.mkdir(parents=True, exist_ok=True)
    for name in files:
        (path / name).write_text("x", encoding="utf-8")


def test_check_lesson_complete(tmp_path):
    lesson = tmp_path / "01_demo"
    _make_lesson(lesson, m.REQUIRED_FILES)
    assert m.check_lesson(lesson) == []


def test_check_lesson_reports_missing_in_order(tmp_path):
    lesson = tmp_path / "02_demo"
    # 只放 README 和 solutions，其余缺失
    _make_lesson(lesson, ["README.md", "solutions.py"])
    assert m.check_lesson(lesson) == ["metadata.yml", "examples.py", "exercises.py"]


def test_check_course_scans_all(tmp_path):
    _make_lesson(tmp_path / "01_a", m.REQUIRED_FILES)
    _make_lesson(tmp_path / "02_b", ["README.md"])
    report = m.check_course(tmp_path)
    assert set(report) == {"01_a", "02_b"}
    assert report["01_a"] == []
    assert "metadata.yml" in report["02_b"]


def test_format_report_markdown(tmp_path):
    _make_lesson(tmp_path / "01_a", m.REQUIRED_FILES)
    report = m.check_course(tmp_path)
    out = m.format_report(report, fmt="markdown")
    assert "| Lesson |" in out
    assert "01_a" in out


def test_format_report_rejects_bad_format():
    import pytest

    with pytest.raises(ValueError):
        m.format_report({}, fmt="xml")
