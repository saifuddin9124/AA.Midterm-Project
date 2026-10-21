"""
Unit and Functional Tests for Insertion Sort and Selection Sort
Algorithm Analysis (2019G3009)
Student: Saifuddin Sayyaf (ID: 2422190016)
"""

import unittest
from insertion_sort import insertion_sort
from selection_sort import selection_sort


class ElementWithId:
    """Helper class to test algorithm stability."""
    def __init__(self, key: int, original_id: int):
        self.key = key
        self.original_id = original_id
        
    def __lt__(self, other):
        return self.key < other.key
        
    def __gt__(self, other):
        return self.key > other.key
        
    def __eq__(self, other):
        return self.key == other.key
        
    def __repr__(self):
        return f"({self.key}, #{self.original_id})"


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([], []),
            ([42], [42]),
            ([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([7, 7, 7, 7, 7], [7, 7, 7, 7, 7]),
            ([-3, 10, -8, 0, 5, -1], [-8, -3, -1, 0, 5, 10]),
            ([100, -50, 200, 0, -100, 50], [-100, -50, 0, 50, 100, 200]),
        ]

    def test_insertion_sort_correctness(self):
        for raw, expected in self.test_cases:
            with self.subTest(raw=raw):
                self.assertEqual(insertion_sort(raw.copy()), expected)

    def test_selection_sort_correctness(self):
        for raw, expected in self.test_cases:
            with self.subTest(raw=raw):
                self.assertEqual(selection_sort(raw.copy()), expected)

    def test_stability(self):
        # Array with duplicate keys: two 5s with distinct IDs (A:1, B:2)
        items_insertion = [
            ElementWithId(5, 1),
            ElementWithId(2, 1),
            ElementWithId(5, 2),
            ElementWithId(1, 1),
        ]
        items_selection = [
            ElementWithId(5, 1),
            ElementWithId(2, 1),
            ElementWithId(5, 2),
            ElementWithId(1, 1),
        ]
        
        sorted_insertion = insertion_sort(items_insertion)
        # Insertion Sort must be stable: (5, #1) comes before (5, #2)
        fives_ins = [x.original_id for x in sorted_insertion if x.key == 5]
        self.assertEqual(fives_ins, [1, 2], "Insertion sort must be stable!")
        
        sorted_selection = selection_sort(items_selection)
        # In selection sort, the first element (5, #1) is swapped with (1, #1),
        # placing (5, #1) after (5, #2). Thus it becomes unstable.
        fives_sel = [x.original_id for x in sorted_selection if x.key == 5]
        self.assertEqual(fives_sel, [2, 1], "Standard selection sort is unstable!")


if __name__ == "__main__":
    unittest.main()
