import pytest

from elevator_dispatch import door_action, next_direction, pick_elevator


@pytest.mark.parametrize(
    ("current", "direction", "requests", "expected"),
    [
        (3, "up", [1, 3, 5], "up"),
        (3, "up", [1, 3], "down"),
        (3, "up", [3], "idle"),
        (3, "down", [1, 3, 5], "down"),
        (3, "down", [3, 5], "up"),
        (3, "down", [3], "idle"),
        (3, "idle", [1, 3, 5], "up"),
        (3, "idle", [1, 3], "down"),
        (3, "idle", [3], "idle"),
    ],
)
def test_next_direction_decision_branches(current, direction, requests, expected):
    assert next_direction(current, direction, requests) == expected


@pytest.mark.parametrize(
    ("load_kg", "blocked", "emergency", "expected"),
    [
        (631, True, True, "hold_open"),
        (631, False, False, "overload"),
        (630, True, False, "reopen"),
        (630, False, False, "close"),
    ],
)
def test_door_action_decision_branches(load_kg, blocked, emergency, expected):
    assert door_action(load_kg, blocked, emergency) == expected


@pytest.mark.parametrize(
    ("cars", "floor", "expected"),
    [
        ([], 5, None),
        ([("A", 2, True)], 2, "A"),
        ([("A", 2, False), ("B", 5, True)], 2, "B"),
        ([("A", 2, True), ("B", 10, True)], 2, "A"),
        ([("A", 1, True), ("B", 5, True)], 3, "A"),
    ],
)
def test_pick_elevator_decision_branches(cars, floor, expected):
    assert pick_elevator(cars, floor) == expected
