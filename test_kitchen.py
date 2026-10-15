# Test list:
# [ ] 200 g x 3 = 600 g
# [ ] Multiplication does not modify the original
# [ ] Same amount and unit are equal
# [ ] 1 oz is not the same as 1 g
# [ ] 200 g + 300 g = 500 g
# [ ] Mixed addition using a conversion rate
# [ ] Multiply a sum (optional)

from kitchen import Quantity


def test_multiplication():
    flour = Quantity(200)
    flour.times(3)
    assert flour.amount == 600

def test_multiplication():
    flour = Quantity(200)
    assert flour.times(3).amount == 600


def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200)

    assert flour.times(3).amount == 600
    assert flour.times(2).amount == 400
    assert flour.amount == 200
    
def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)