import pytest

from course_loader import DATA, load

m = load("05_decorators")


def test_memoize_caches_repeated_args():
    calls = {"n": 0}

    @m.memoize
    def square(x):
        calls["n"] += 1
        return x * x

    assert square(3) == 9
    assert square(3) == 9
    assert calls["n"] == 1  # 第二次命中缓存


def test_memoize_preserves_name():
    @m.memoize
    def foo(x):
        return x

    assert foo.__name__ == "foo"


def test_retry_succeeds_after_failures():
    attempts = {"n": 0}

    @m.retry(times=3)
    def flaky():
        attempts["n"] += 1
        if attempts["n"] < 3:
            raise ValueError("not yet")
        return "ok"

    assert flaky() == "ok"
    assert attempts["n"] == 3


def test_retry_raises_after_exhaustion():
    @m.retry(times=2, exceptions=(KeyError,))
    def always():
        raise KeyError("boom")

    with pytest.raises(KeyError):
        always()


def test_retry_rejects_bad_times():
    with pytest.raises(ValueError):
        m.retry(times=0)


def test_parse_log_line():
    line = '10.0.0.1 - - [12/Jan/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1043'
    rec = m.parse_log_line(line)
    assert rec == {
        "ip": "10.0.0.1",
        "method": "GET",
        "path": "/index.html",
        "status": 200,
        "bytes": 1043,
    }
    assert m.parse_log_line("not a log line") is None


def test_status_counts():
    counts = m.status_counts(DATA / "access.log")
    assert counts == {200: 6, 404: 3, 500: 2, 403: 1}
