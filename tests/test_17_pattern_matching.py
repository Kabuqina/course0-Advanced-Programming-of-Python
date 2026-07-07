import sys

import pytest

from course_loader import DATA, load

pytestmark = pytest.mark.skipif(
    sys.version_info < (3, 10), reason="structural pattern matching needs Python 3.10+"
)

m = load("17_pattern_matching")


def test_describe_event_variants():
    assert m.describe_event({"type": "click", "x": 10, "y": 20}) == "click at (10, 20)"
    assert m.describe_event({"type": "key", "key": "Enter"}) == "key Enter"
    assert m.describe_event({"type": "scroll", "dy": -3}) == "scroll down 3"
    assert m.describe_event({"type": "scroll", "dy": 2}) == "scroll up 2"
    assert m.describe_event({"type": "resize", "width": 800, "height": 600}) == "resize to 800x600"
    assert m.describe_event({"type": "custom"}) == "unknown event: custom"
    assert m.describe_event({"foo": "bar"}) == "malformed event"


def test_load_and_count_events():
    events = m.load_events(DATA / "events.json")
    assert len(events) == 6
    assert m.count_event_types(events) == {"click": 2, "key": 2, "scroll": 1, "resize": 1}


def test_count_malformed():
    assert m.count_event_types([{"type": "click"}, {"no_type": 1}]) == {
        "click": 1,
        "_malformed": 1,
    }


def test_shape_area():
    assert m.shape_area({"kind": "rect", "w": 3, "h": 4}) == 12.0
    assert m.shape_area({"kind": "square", "side": 5}) == 25.0
    assert round(m.shape_area({"kind": "circle", "r": 1}), 5) == 3.14159


def test_shape_area_unknown_raises():
    with pytest.raises(ValueError):
        m.shape_area({"kind": "triangle", "base": 2, "height": 3})
