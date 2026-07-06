import pytest

from course_loader import DATA, load

m = load("05_metaprogramming")


def test_book_valid():
    book = m.Book("Fluent Python", "Ramalho", 2022, 59.9)
    assert book.title == "Fluent Python"
    assert book.year == 2022
    assert book.price == 59.9


def test_typed_rejects_wrong_type():
    with pytest.raises(TypeError):
        m.Book("T", "A", "not-an-int", 10.0)


def test_positive_rejects_non_positive():
    with pytest.raises(ValueError):
        m.Book("T", "A", 2020, 0)


def test_positive_rejects_non_number():
    with pytest.raises(TypeError):
        m.Book("T", "A", 2020, "free")


def test_init_subclass_registry():
    m.Plugin.registry.clear()

    class Alpha(m.Plugin):
        pass

    class Beta(m.Plugin):
        pass

    assert m.Plugin.registry.get("Alpha") is Alpha
    assert m.Plugin.registry.get("Beta") is Beta


def test_make_books_from_dataset():
    books = m.make_books(DATA / "books.json")
    assert len(books) == 8
    assert all(isinstance(b, m.Book) for b in books)
