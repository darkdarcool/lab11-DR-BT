# https://github.com/darkdarcool/lab11-DR-BT
# Partner 1: Darren Reddy
# Partner 2: Bryan Tran


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(9, 3), 27)
        self.assertEqual(mul(10, 2), 20)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(15, 5), 3)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(1, 1), math.sqrt(2))
        self.assertEqual(hypotenuse(-5, -12), 13.0)


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(9), 3.0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()