import useful_things

def test_add(x, y):
    assert useful_things.add(x, y) == x + y


def test_subtract(x, y):
    assert useful_things.subtract(x, y) == x - y
