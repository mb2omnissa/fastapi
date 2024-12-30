from ..app.calulations import add, subtract, multiply , divide, BankAccount
import pytest

# @pytest.mark.parametrize("num1, num2, expected", [
#     (1, 2, 3),
#     (2, 1, 3),
#     (3, 2, 5),
#     (4, 3, 7),
#     (12, 8, 20)
# ])
# def test_add(num1, num2, expected):
#     print("testing add function")
#
#     assert add(num1, num2) == expected
#
# def test_subtract():
#     print("testing subtract function")
#     assert subtract(6, 2) == 4
#
# def test_multiply():
#     print("testing multiply function")
#     assert multiply(1, 2) == 2
#
# def test_divide():
#     print("testing divide function")
#     assert divide(4, 2) == 2

# test_add()
# test_subtract()
# test_multiply()
# test_divide()

def test_bank_set_initial_amount():
    bank_account = BankAccount(50)
    assert bank_account.balance == 50