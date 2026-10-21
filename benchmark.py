"""
Empirical Benchmark Suite for Insertion Sort vs. Selection Sort
Algorithm Analysis (2019G3009)
Student: Saifuddin Sayyaf (ID: 2422190016)

Measures:
1. CPU Time (milliseconds) using time.perf_counter()
2. Peak Auxiliary Memory (KiB) using tracemalloc
3. Algorithmic Operations (Comparisons & Swaps/Shifts)
Across Best, Average, and Worst Case scenarios for multiple input sizes.
"""

import time
import random
import tracemalloc
from typing import List, Callable, Tuple, Dict, Any
from insertion_sort import insertion_sort, insertion_sort_instrumented
from selection_sort import selection_sort, selection_sort_instrumented


def generate_dataset(size: int, case: str) -> List[int]:
    """Generates test dataset based on case type."""
    if case == "Best":
        # Sorted array
        return list(range(size))
    elif case == "Worst":
        # Reverse sorted array
        return list(range(size, 0, -1))
    elif case == "Average":
        # Randomly shuffled array with fixed seed for reproducibility
        rng = random.Random(42 + size)
        arr = list(range(size))
        rng.shuffle(arr)
        return arr
    else:
        raise ValueError(f"Unknown case: {case}")


def measure_performance(sort_fn: Callable[[List[int]], List[int]], data: List[int]) -> Tuple[float, float]:
    """
    Measures CPU execution time (ms) and peak memory (KiB).
    """
    arr_copy = data.copy()
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    sort_fn(arr_copy)
    
    end_time = time.perf_counter()
    _, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    time_ms = (end_time - start_time) * 1000.0
    mem_kib = peak_mem / 1024.0
    return time_ms, mem_kib


def run_full_benchmark() -> List[Dict[str, Any]]:
    sizes = [100, 500, 1000, 2000, 5000]
    cases = ["Best", "Average", "Worst"]
    
    print("=" * 80)
    print("RUNNING BENCHMARKS: INSERTION SORT VS SELECTION SORT")
    print("=" * 80)
    
    results = []
    
    for case in cases:
        print(f"\n--- Testing Scenario: {case} Case ---")
        for size in sizes:
            dataset = generate_dataset(size, case)
            
            # Measure Insertion Sort
            time_ins, mem_ins = measure_performance(insertion_sort, dataset)
            _, comps_ins, ops_ins = insertion_sort_instrumented(dataset.copy())
            
            # Measure Selection Sort
            time_sel, mem_sel = measure_performance(selection_sort, dataset)
            _, comps_sel, ops_sel = selection_sort_instrumented(dataset.copy())
            
            results.append({
                "case": case,
                "size": size,
                "time_ins": time_ins,
                "mem_ins": mem_ins,
                "comps_ins": comps_ins,
                "ops_ins": ops_ins,
                "time_sel": time_sel,
                "mem_sel": mem_sel,
                "comps_sel": comps_sel,
                "ops_sel": ops_sel,
            })
            
            print(f"Size: {size:>5} | "
                  f"Insertion: {time_ins:>8.3f} ms, {mem_ins:>6.2f} KiB | "
                  f"Selection: {time_sel:>8.3f} ms, {mem_sel:>6.2f} KiB")
            
    print("\n" + "=" * 80)
    print("BENCHMARK SUMMARY (MARKDOWN FORMAT)")
    print("=" * 80)
    
    print("\n### CPU Execution Time (ms) & Peak Memory (KiB)\n")
    print("| Scenario | Size (N) | Insertion Sort Time (ms) | Selection Sort Time (ms) | Insertion Peak Mem (KiB) | Selection Peak Mem (KiB) |")
    print("| :--- | :--- | :--- | :--- | :--- | :--- |")
    for r in results:
        print(f"| {r['case']} | {r['size']} | {r['time_ins']:.3f} | {r['time_sel']:.3f} | {r['mem_ins']:.2f} | {r['mem_sel']:.2f} |")
        
    print("\n### Operation Counts: Comparisons & Shifts / Swaps\n")
    print("| Scenario | Size (N) | Ins. Comparisons | Sel. Comparisons | Ins. Shifts | Sel. Swaps |")
    print("| :--- | :--- | :--- | :--- | :--- | :--- |")
    for r in results:
        print(f"| {r['case']} | {r['size']} | {r['comps_ins']:,} | {r['comps_sel']:,} | {r['ops_ins']:,} | {r['ops_sel']:,} |")

    return results


if __name__ == "__main__":
    run_full_benchmark()
