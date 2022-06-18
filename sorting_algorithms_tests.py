import unittest
import random

from sorting_algorithms import bubble_sort


class SortingAlgorithmTests(unittest.TestCase):
    @staticmethod
    def __generate_random_array(arr_length):
        random_arr = list()
        for element in range(arr_length):
            random_arr += [random.randint(0, arr_length * 2)]
        return random_arr

    def test_bubble_sort(self):
        for arrays in range(2 ** 4):  # test on 2 ** 4 arrays
            arr_length = random.randint(2 ** 4, 2 ** 8)
            unsorted_arr = self.__generate_random_array(arr_length)
            expected_arr = sorted(unsorted_arr)
            actual_arr = bubble_sort(unsorted_arr)
            self.assertListEqual(expected_arr, actual_arr)


if __name__ == '__main__':
    unittest.main()
