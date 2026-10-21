"""
Selection Sort Implementation
Algorithm Analysis (2019G3009)
Student: Saifuddin Sayyaf (ID: 2422190016)
Lecturer: Dr. Coşkun Şahin
Faculty of Engineering and Architecture / Software Engineering
İstanbul Esenyurt University
"""

from typing import List, Any, Tuple


def selection_sort(arr: List[Any]) -> List[Any]:
    """
    Sorts a list in ascending order using the In-Place Selection Sort algorithm.
    
    Time Complexity:
        - Best Case:    O(n^2)   (Always scans entire remaining subarray)
        - Average Case: O(n^2)   (Requires n(n-1)/2 comparisons)
        - Worst Case:   O(n^2)   (Requires n(n-1)/2 comparisons)
        
    Auxiliary Space Complexity:
        - O(1) in-place auxiliary memory
        
    Stability:
        - Unstable in standard array swap implementation.
        
    Args:
        arr: The list of elements to be sorted (modified in-place).
        
    Returns:
        The sorted list.
    """
    n = len(arr)
    # Traverse through all array elements except the last
    for i in range(n - 1):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element of unsorted part
        # Only swap if min_idx has changed (minor optimization to avoid redundant self-swap)
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    return arr


def selection_sort_instrumented(arr: List[Any]) -> Tuple[List[Any], int, int]:
    """
    Instrumented version that tracks comparisons and swaps.
    Useful for detailed algorithmic evaluation and verification.
    """
    comparisons = 0
    swaps = 0
    n = len(arr)
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            
    return arr, comparisons, swaps


if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11]
    print("Original array:", sample)
    sorted_arr, comps, swaps = selection_sort_instrumented(sample.copy())
    print("Sorted array:  ", sorted_arr)
    print(f"Metrics: Comparisons = {comps}, Swaps = {swaps}")
