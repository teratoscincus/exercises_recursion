import unittest


def flatten_list_recursively(l, flat_list=[]):
    # Base Case
    if not l:
        return l

    # Recursive Case
    if isinstance(l[0], list):
        # Separate the first element and the rest of the list.
        return flatten_list_recursively(l[0]) + flatten_list_recursively(l[1:])
    else:
        # Add the first element and flatten the rest of the list.
        return l[:1] + flatten_list_recursively(l[1:])


class FlattenNestedListRecursivelyTestCase(unittest.TestCase):
    def test_non_nested(self):
        nested_list = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(flatten_list_recursively(nested_list), expected_result)

    def test_nested_list(self):
        nested_list = [[1, 2]]
        expected_result = [1, 2]
        self.assertEqual(flatten_list_recursively(nested_list), expected_result)

    def test_one_nested_level(self):
        nested_list = [[1, 2], [3, 4]]
        expected_result = [1, 2, 3, 4]
        self.assertEqual(flatten_list_recursively(nested_list), expected_result)

    def test_mixed_nested_and_not_nested(self):
        nested_list = [[1, [8, 9]], [3, 4]]
        expected_result = [1, 8, 9, 3, 4]
        self.assertEqual(flatten_list_recursively(nested_list), expected_result)

    def test_two_levels_nested(self):
        nested_list = [[1, [2, 3]], [[4, 5], 6], 7]
        expected_result = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(flatten_list_recursively(nested_list), expected_result)


if __name__ == "__main__":
    unittest.main()
