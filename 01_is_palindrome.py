import unittest


def is_palindrome(text: str) -> bool:
    """A recursive function that returns True if given sting is a palindrome."""
    # Remove space characters
    text = text.replace(" ", "")

    # Base case
    if len(text) == 1 or len(text) == 0:
        return True

    # Recursive case
    else:
        if text[0] == text[-1]:
            return is_palindrome(text[1:-1])
        else:
            return False


class IsPalindromeTestCase(unittest.TestCase):
    def test_base_case(self):
        self.assertTrue(is_palindrome("xx"))

    def test_even_palindrome(self):
        self.assertTrue(is_palindrome("noon"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("tool"))

    def test_odd_palindrome(self):
        self.assertTrue(is_palindrome("pop"))

    def test_long_palindrome(self):
        self.assertTrue(is_palindrome("tenet"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("never odd or even"))


if __name__ == "__main__":
    unittest.main()
