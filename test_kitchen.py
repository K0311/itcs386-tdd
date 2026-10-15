# Test list:
# [ ] 200 g x 3 = 600 g
# [ ] Multiplication does not modify the original
# [ ] Same amount and unit are equal
# [ ] 1 oz is not the same as 1 g
# [ ] 200 g + 300 g = 500 g
# [ ] Mixed addition using a conversion rate
# [ ] Multiply a sum (optional)
# [ ] Consider hashing if quantities need set or dictionary-key support

from kitchen import Quantity


def test_multiplication():
    flour = Quantity(200, "g")
    assert flour.times(3) == Quantity(600, "g")


def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200, "g")

    assert flour.times(3) == Quantity(600, "g")
    assert flour.times(2) == Quantity(400, "g")
    assert flour == Quantity(200, "g")


def test_equality():
    assert Quantity(200, "g") == Quantity(200, "g")
    assert Quantity(200, "g") != Quantity(300, "g")


def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")