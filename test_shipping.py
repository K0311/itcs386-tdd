import pytest
from shipping import shipping_fee


# Rule 1: zero and negative weights must raise ValueError.
@pytest.mark.parametrize("weight", [-1, 0])
def test_invalid_weight_is_rejected(weight):
    with pytest.raises(ValueError, match="more than 0"):
        shipping_fee(weight)


# Rule 2: exactly 1 kg must cost 40 baht.
# Rule 4: a started kilogram above 5 kg must be rounded up.
@pytest.mark.parametrize("weight, expected", [
    (0.1, 40),
    (0.5, 40),
    (1.0, 40),
    (1.01, 60),
    (3.0, 60),
    (5.0, 60),
    (5.01, 70),
    (5.2, 70),
    (6.0, 70),
    (6.1, 80),
    (7.0, 80),
])
def test_shipping_fee(weight, expected):
    assert shipping_fee(weight) == expected