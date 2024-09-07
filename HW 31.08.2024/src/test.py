import unittest
from main import SortList

class TestSortList(unittest.TestCase):
    # Положительные тесты
    def test_sorted_list(self):
        self.assertEqual(SortList([3, 1, 2]), [1, 2, 3])

    def test_sorted_list_with_duplicates(self):
        self.assertEqual(SortList([3, 1, 2, 1]), [1, 1, 2, 3])

    def test_sorted_list_with_negative_numbers(self):
        self.assertEqual(SortList([-1, -3, -2]), [-3, -2, -1])

    def test_sorted_list_with_mixed_numbers(self):
        self.assertEqual(SortList([3, -1, 2, 0]), [-1, 0, 2, 3])

    def test_sorted_list_empty(self):
        self.assertEqual(SortList([]), [])

    def test_sorted_list_single_element(self):
        self.assertEqual(SortList([1]), [1])

    # Отрицательные тесты
    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            SortList("not a list")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            SortList(None)

    def test_list_with_non_comparable_elements(self):
        with self.assertRaises(TypeError):
            SortList([1, "two", 3])

if __name__ == '__main__':
    unittest.main()