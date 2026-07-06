import asyncio

import pytest

from course_loader import DATA, load

m = load("04_concurrency_asyncio")
BOOKS = m.load_books(DATA / "books.json")


def test_fetch_all_returns_all_in_order():
    res = asyncio.run(m.fetch_all(BOOKS))
    assert len(res) == len(BOOKS)
    assert res[0]["title"] == BOOKS[0]["title"]


def test_total_price_matches_sum():
    total = asyncio.run(m.total_price(BOOKS))
    expected = round(sum(float(b["price"]) for b in BOOKS), 2)
    assert total == expected


def test_bounded_gather_runs_all():
    factories = [(lambda b=b: m.fetch_book(b)) for b in BOOKS]
    res = asyncio.run(m.bounded_gather(factories, limit=3))
    assert len(res) == len(BOOKS)


def test_bounded_gather_rejects_bad_limit():
    with pytest.raises(ValueError):
        asyncio.run(m.bounded_gather([], 0))
