import unittest
from calc import aec_division


class TestDivide(unittest.TestCase):

    def test_division(self):
        arg_ints = [20, 5]
        div_result = aec_division(arg_ints)
        self.assertEqual(div_result, 4)

    def test_divide_by_zero_is_zero(self):
        arg_ints = [20, 0]
        div_result = aec_division(arg_ints)
        self.assertEqual(div_result, 0)

    def test_raise_alarm(self):
        arg_ints = [20, 4, 5]
        with self.assertRaisesRegex(Exception, "More than two too much") as context:
            aec_division(arg_ints)


if __name__ == "__main__":
    unittest.main()