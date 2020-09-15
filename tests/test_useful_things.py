import useful_things
from hypothesis import given
import hypothesis.strategies as st


@given(st.integers(), st.integers())
def test_add(x, y):
    assert useful_things.add(x, y) == x + y

