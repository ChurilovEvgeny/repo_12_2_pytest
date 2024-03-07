import pytest

from utils import arrs

@pytest.fixture
def coll_1_2_3_4():
    return [1, 2 ,3, 4]

@pytest.fixture
def coll_1_2_3():
    return [1, 2 ,3]

@pytest.fixture
def coll_2_3():
    return [2 ,3]

@pytest.fixture
def coll_empty():
    return []

def test_get(coll_empty, coll_1_2_3):
    assert arrs.get(coll_1_2_3, 1, "test") == 2
    assert arrs.get(coll_empty, 0, "test") == "test"


def test_slice(coll_empty, coll_1_2_3, coll_2_3, coll_1_2_3_4):
    assert arrs.my_slice(coll_1_2_3_4, 1, 3) == coll_2_3
    assert arrs.my_slice(coll_1_2_3, 1) == coll_2_3
    assert arrs.my_slice(coll_empty, 1) == coll_empty
    assert arrs.my_slice(coll_1_2_3) == coll_1_2_3
