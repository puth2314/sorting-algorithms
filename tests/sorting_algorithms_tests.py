import unittest
import random

from src.sorting_algorithms import bubble_sort


class SortingAlgorithmTests(unittest.TestCase):

    @staticmethod
    def gen_random_array(arr_length):
        random_arr = list()
        for element in range(arr_length):
            random_arr += [random.randint(0, arr_length * 2)]
        return random_arr

    # TEST BUBBLE SORT

    def test_bubble_sort_empty(self):
        unsorted_arr = []
        expected_arr = []
        actual_arr = bubble_sort(unsorted_arr)
        self.assertListEqual(expected_arr, actual_arr)

    def test_bubble_sort_random(self):
        unsorted_arr = self.gen_random_array(random.randint(2 ** 4, 2 ** 8))
        expected_arr = sorted(unsorted_arr)
        actual_arr = bubble_sort(unsorted_arr)
        self.assertListEqual(expected_arr, actual_arr)


if __name__ == '__main__':
    unittest.main()
