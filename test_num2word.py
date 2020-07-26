import unittest

from num2word import get_tens_value, get_hundreds_value, get_thousands_value, get_num_thousands
from num2word import num2word


class HelpersTestCase(unittest.TestCase):
    def test_tens_value(self):
        numbers = [394, 23, 9891, 111, 104]
        expecteds = [9, 2, 9, 1, 0]
        for n, expected in zip(numbers, expecteds):
            got = get_tens_value(n)
            self.assertEqual(expected, got)

    def test_hundreds_value(self):
        numbers = [394, 23, 9891, 111, 12104]
        expecteds = [3, 0, 8, 1, 1]
        for n, expected in zip(numbers, expecteds):
            got = get_hundreds_value(n)
            self.assertEqual(expected, got)

    def test_thousands_value(self):
        numbers = [1000, 8972, 982718, 98, 127, 7654]
        expecteds = [1, 8, 2, 0, 0, 7]
        for n, expected in zip(numbers, expecteds):
            got = get_thousands_value(n)
            self.assertEqual(expected, got)

    def test_num_thousands(self):
        numbers = [1000, 8972, 982718, 98, 127, 7654, 80190]
        expecteds = [1, 8, 982, 0, 0, 7, 80]
        for n, expected in zip(numbers, expecteds):
            got = get_num_thousands(n)
            self.assertEqual(expected, got)


class Num2WordTestCase(unittest.TestCase):
    def test_zero_to_nineteen(self):
        expected_word = "zero"
        got_word = num2word(0)
        self.assertEqual(expected_word, got_word)

        expected_word = "eight"
        got_word = num2word(8)
        self.assertEqual(expected_word, got_word)

    def test_two_digit(self):
        expected_word = "thirty four"
        got_word = num2word(34)
        self.assertEqual(expected_word, got_word)

        expected_word = "seventy"
        got_word = num2word(70)
        self.assertEqual(expected_word, got_word)

    def test_three_digit(self):
        expected_word = "seven hundred and eighty one"
        got_word = num2word(781)
        self.assertEqual(expected_word, got_word)

        expected_word = "one hundred"
        got_word = num2word(100)
        self.assertEqual(expected_word, got_word)

        expected_word = "two hundred and fifty"
        got_word = num2word(250)
        self.assertEqual(expected_word, got_word)

        expected_word = "three hundred and one"
        got_word = num2word(301)
        self.assertEqual(expected_word, got_word)

    def test_four_digit(self):
        expected_word = "two thousand four hundred and sixty nine"
        got_word = num2word(2469)
        self.assertEqual(expected_word, got_word)

        expected_word = "four thousand"
        got_word = num2word(4000)
        self.assertEqual(expected_word, got_word)

        expected_word = "six thousand and one hundred"
        got_word = num2word(6100)
        self.assertEqual(expected_word, got_word)

    def test_five_digit(self):
        expected_word = "twenty two thousand four hundred and sixty nine"
        got_word = num2word(22469)
        self.assertEqual(expected_word, got_word)

        expected_word = "thirty thousand"
        got_word = num2word(30000)
        self.assertEqual(expected_word, got_word)

        expected_word = "thirty thousand and two"
        got_word = num2word(30002)
        self.assertEqual(expected_word, got_word)

        expected_word = "twelve thousand and fifteen"
        got_word = num2word(12015)
        self.assertEqual(expected_word, got_word)

        expected_word = "sixty thousand and four hundred"
        got_word = num2word(60400)
        self.assertEqual(expected_word, got_word)

    def test_six_digit(self):
        expected_word = "three hundred and forty nine thousand and sixty two"
        got_word = num2word(349062)
        self.assertEqual(expected_word, got_word)

        expected_word = "eight hundred thousand"
        got_word = num2word(800000)
        self.assertEqual(expected_word, got_word)


if __name__ == '__main__':
    unittest.main()
