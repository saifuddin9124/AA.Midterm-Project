"""
Insertion Sort Implementation
Algorithm Analysis (2019G3009)
Student: Saifuddin Sayyaf (ID: 2422190016)
Lecturer: Dr. Coşkun Şahin
Faculty of Engineering and Architecture / Software Engineering
İstanbul Esenyurt University
"""

from typing import List, Any, Tuple


def insertion_sort(arr: List[Any]) -> List[Any]:
    """
    Sorts a list in ascending order using the In-Place Insertion Sort algorithm.
    
    Time Complexity:
        - Best Case:    O(n)     (Array is already sorted)
        - Average Case: O(n^2)   (Array is in random order)
        - Worst Case:   O(n^2)   (Array is sorted in reverse order)
        
    Auxiliary Space Complexity:
        - O(1) in-place auxiliary memory
        
    Stability:
        - Stable: preserves relative order of duplicate elements.
        
    Args:
        arr: The list of elements to be sorted (modified in-place).
        
    Returns:
        The sorted list.
    """
    n = len(arr)
    # Traverse through 1 to len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position.
        # Using '>' ensures stability (equal elements are not swapped).
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr


def insertion_sort_instrumented(arr: List[Any]) -> Tuple[List[Any], int, int]:
    """
    Instrumented version that tracks comparisons, shifts, and memory reads/writes.
    Useful for detailed algorithmic evaluation and verification.
    """
    comparisons = 0
    shifts = 0
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
        
    return arr, comparisons, shifts


if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11]
    print("Original array:", sample)
    sorted_arr, comps, shifts = insertion_sort_instrumented(sample.copy())
    print("Sorted array:  ", sorted_arr)
    print(f"Metrics: Comparisons = {comps}, Shifts = {shifts}")
