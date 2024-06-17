import unittest
from calc import aec_subtract 
# Mad Mad, so this is how a function from a python file can be imported into another python file
# Sooooo, it's like the python file is now a module? interesting.

class TestSubtract(unittest.TestCase):

    def test_subtract(self):
        arg_ints = [20, 5]
        sub_result = aec_subtract(arg_ints)
        self.assertEqual(sub_result, 15)

    def test_cant_go_below_zero(self):
        arg_ints = [5, 20]
        sub_result = aec_subtract(arg_ints)
        self.assertEqual(sub_result, 0)

    def test_raise_alarm(self):
        arg_ints = [20, 4, 5]
        with self.assertRaisesRegex(Exception, "More than two too much") as context:
            aec_subtract(arg_ints)


if __name__ == "__main__":
    unittest.main()