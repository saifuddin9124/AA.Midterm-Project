# Project Assignment: Comparative Analysis of Insertion Sort and Selection Sort

**Course:** Algorithm Analysis (2019G3009)  
**Academic Term:** 2025–2026 Fall Semester  
**Faculty:** Faculty of Engineering and Architecture  
**Department:** Software Engineering (English)  
**Institution:** İstanbul Esenyurt University  
**Lecturer:** Dr. Coşkun Şahin  

**Student Information:**  
* **Name & Surname:** Saifuddin Sayyaf  
* **Student ID:** 2422190016  
* **Repository Collaborator:** `drcoskuns`  

---

## Table of Contents
1. [Executive Summary](#1-executive-summary)
2. [Algorithm Explanations](#2-algorithm-explanations)
   - [2.1 Insertion Sort](#21-insertion-sort)
   - [2.2 Selection Sort](#22-selection-sort)
3. [Theoretical Complexity Analysis (CPU & Memory)](#3-theoretical-complexity-analysis-cpu--memory)
   - [3.1 Workload on CPU (Time Complexity)](#31-workload-on-cpu-time-complexity)
   - [3.2 Workload on Memory (Space Complexity)](#32-workload-on-memory-space-complexity)
   - [3.3 Algorithmic Properties: Stability & Adaptivity](#33-algorithmic-properties-stability--adaptivity)
4. [Empirical Benchmarks & Experimental Results](#4-empirical-benchmarks--experimental-results)
   - [4.1 Experimental Methodology](#41-experimental-methodology)
   - [4.2 CPU Execution Time & Memory Usage](#42-cpu-execution-time--memory-usage)
   - [4.3 Operational Metrics: Comparisons vs. Swaps/Shifts](#43-operational-metrics-comparisons-vs-swapsshifts)
   - [4.4 Analysis of Experimental Findings](#44-analysis-of-experimental-findings)
5. [Comparison & Best Use Cases](#5-comparison--best-use-cases)
   - [5.1 Comprehensive Comparison Matrix](#51-comprehensive-comparison-matrix)
   - [5.2 When to Choose Insertion Sort](#52-when-to-choose-insertion-sort)
   - [5.3 When to Choose Selection Sort](#53-when-to-choose-selection-sort)
6. [Project Structure & Execution Guide](#6-project-structure--execution-guide)
7. [AI Utilization Rules and Ethic Codes](#7-ai-utilization-rules-and-ethic-codes)

---

## 1. Executive Summary

This report delivers a rigorous comparative analysis of two fundamental comparison-based sorting algorithms: **Insertion Sort** and **Selection Sort**. Although both algorithms belong to the $O(n^2)$ time-complexity family in their average and worst cases, their internal mechanics, data-movement patterns, cache behaviors, adaptivity, and stability diverge significantly.

Through theoretical derivations and empirical benchmarks across three data configurations (**Best Case**, **Average Case**, and **Worst Case**) spanning sizes up to $n = 5,000$, this investigation highlights:
1. **Insertion Sort's Adaptive Advantage:** Achieves near-linear $\mathcal{O}(n)$ runtime on sorted and presorted lists, making it up to **$935\times$ faster** than Selection Sort on sorted inputs.
2. **Selection Sort's Minimal Write Property:** Restricts memory writes to strictly $\mathcal{O}(n)$ swaps (at most $n-1$), making it twice as fast as Insertion Sort in worst-case reverse-sorted scenarios where shifting memory overhead dominates execution time.

---

## 2. Algorithm Explanations

### 2.1 Insertion Sort

#### Mechanics and Intuition
Insertion Sort operates analogously to how a human sorts a hand of playing cards. The array is conceptually divided into two partitions: a **sorted subarray** on the left and an **unsorted subarray** on the right. 

1. The first element (`arr[0]`) is considered trivially sorted.
2. The algorithm advances index $i$ from $1$ to $n-1$, picking `key = arr[i]`.
3. The `key` is compared backward against elements in the sorted partition (`arr[j]` for $j = i-1$ down to $0$).
4. Elements greater than `key` are shifted one position to the right (`arr[j+1] = arr[j]`).
5. As soon as an element $\le \text{key}$ or the boundary is reached, `key` is dropped into the vacated slot (`arr[j+1] = key`).

#### Pseudocode
```text
algorithm InsertionSort(A):
    for i = 1 to length(A) - 1:
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A
```

#### Step-by-Step Trace: `[64, 25, 12, 22, 11]`
* **Initial:** `[64 | 25, 12, 22, 11]` (Left of `|` is sorted)
* **Step 1 ($i=1$, key=25):** 64 > 25 $\rightarrow$ shift 64 $\rightarrow$ `[25, 64 | 12, 22, 11]`
* **Step 2 ($i=2$, key=12):** 64 > 12, 25 > 12 $\rightarrow$ shift 64, 25 $\rightarrow$ `[12, 25, 64 | 22, 11]`
* **Step 3 ($i=3$, key=22):** 64 > 22, 25 > 22, 12 < 22 $\rightarrow$ shift 64, 25 $\rightarrow$ `[12, 22, 25, 64 | 11]`
* **Step 4 ($i=4$, key=11):** Shift 64, 25, 22, 12 $\rightarrow$ `[11, 12, 22, 25, 64]`

---

### 2.2 Selection Sort

#### Mechanics and Intuition
Selection Sort divides the list into a sorted prefix and an unsorted suffix. It works by repeatedly finding the **minimum** element from the unsorted subarray and placing it at the beginning of the unsorted subarray via an element swap.

1. Loop index $i$ runs from $0$ to $n-2$.
2. Assume the current index is the minimum: `min_idx = i`.
3. Scan all remaining items ($j = i+1$ to $n-1$). If `arr[j] < arr[min_idx]`, update `min_idx = j`.
4. After completing the inner loop scan, swap `arr[i]` with `arr[min_idx]` if `min_idx != i`.

#### Pseudocode
```text
algorithm SelectionSort(A):
    n = length(A)
    for i = 0 to n - 2:
        min_idx = i
        for j = i + 1 to n - 1:
            if A[j] < A[min_idx]:
                min_idx = j
        if min_idx != i:
            swap(A[i], A[min_idx])
    return A
```

#### Step-by-Step Trace: `[64, 25, 12, 22, 11]`
* **Pass 1 ($i=0$):** Find min in `[64, 25, 12, 22, 11]` $\rightarrow$ min is 11. Swap 64 with 11 $\rightarrow$ `[11 | 25, 12, 22, 64]`
* **Pass 2 ($i=1$):** Find min in `[25, 12, 22, 64]` $\rightarrow$ min is 12. Swap 25 with 12 $\rightarrow$ `[11, 12 | 25, 22, 64]`
* **Pass 3 ($i=2$):** Find min in `[25, 22, 64]` $\rightarrow$ min is 22. Swap 25 with 22 $\rightarrow$ `[11, 12, 22 | 25, 64]`
* **Pass 4 ($i=3$):** Find min in `[25, 64]` $\rightarrow$ min is 25. No swap needed $\rightarrow$ `[11, 12, 22, 25 | 64]`
* **Sorted Result:** `[11, 12, 22, 25, 64]`

---

## 3. Theoretical Complexity Analysis (CPU & Memory)

### 3.1 Workload on CPU (Time Complexity)

#### A. Insertion Sort
* **Best Case — Sorted Input:**  
  When the array is already sorted, the `while` loop condition `arr[j] > key` fails on the very first comparison for every element $i$.
  $$\text{Comparisons} = \sum_{i=1}^{n-1} 1 = n - 1 = \mathcal{O}(n)$$
  $$\text{Shifts} = 0$$
  Therefore, the best-case CPU time complexity is **$\mathcal{O}(n)$**.

* **Worst Case — Reverse Sorted Input:**  
  For each key $i$, every element in `arr[0..i-1]` is strictly greater than `key`. The `while` loop runs $i$ times for each $i$.
  $$\text{Comparisons} = \sum_{i=1}^{n-1} i = \frac{n(n-1)}{2} = \mathcal{O}(n^2)$$
  $$\text{Shifts} = \sum_{i=1}^{n-1} i = \frac{n(n-1)}{2} = \mathcal{O}(n^2)$$
  Therefore, the worst-case CPU time complexity is **$\mathcal{O}(n^2)$**.

* **Average Case — Random Input:**  
  On average, each key must be compared with and shifted past half of the elements in the sorted partition:
  $$\text{Comparisons} \approx \sum_{i=1}^{n-1} \frac{i}{2} = \frac{n(n-1)}{4} = \mathcal{O}(n^2)$$
  Therefore, average CPU workload is **$\mathcal{O}(n^2)$**.

#### B. Selection Sort
* **Universal Case (Best, Average, and Worst Case):**  
  Selection Sort unconditionally scans the entirety of the unsorted suffix to find the true minimum element. The inner loop always runs from $j = i+1$ to $n-1$, irrespective of the initial data ordering.
  $$\text{Comparisons} = \sum_{i=0}^{n-2} (n - 1 - i) = (n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2}$$
  * **Best Case:** Array is already sorted $\rightarrow \frac{n(n-1)}{2}$ comparisons, $0$ swaps $\rightarrow \mathcal{O}(n^2)$ CPU time.
  * **Average Case:** Random array $\rightarrow \frac{n(n-1)}{2}$ comparisons, $\mathcal{O}(n)$ swaps $\rightarrow \mathcal{O}(n^2)$ CPU time.
  * **Worst Case:** Reverse sorted array $\rightarrow \frac{n(n-1)}{2}$ comparisons, at most $n-1$ swaps $\rightarrow \mathcal{O}(n^2)$ CPU time.

---

### 3.2 Workload on Memory (Space Complexity)

| Algorithm | Primary Data Storage | Auxiliary / Extra Memory | Memory Access Model |
| :--- | :--- | :--- | :--- |
| **Insertion Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | In-place (1 temporary `key` variable) |
| **Selection Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | In-place (1 temporary `min_idx` pointer) |

* **In-Place Execution:** Both algorithms require only a fixed constant number of scalar memory registers (`i`, `j`, `key`, `min_idx`), achieving strict **$\mathcal{O}(1)$ auxiliary space complexity**.
* **Memory Writes (Bus Traffic & Flash Endurance):**
  * **Insertion Sort:** Writes up to $\mathcal{O}(n^2)$ times (shifting array elements one by one).
  * **Selection Sort:** Writes strictly at most $n-1$ times ($\mathcal{O}(n)$ swaps). When memory writes are physically expensive or wear-limited (e.g., Flash EEPROM memory), Selection Sort imposes vastly lower write wear.

---

### 3.3 Algorithmic Properties: Stability & Adaptivity

* **Stability:**
  * **Insertion Sort is Stable:** A sorting algorithm is stable if it preserves the original relative order of elements with equal keys. In Insertion Sort, `arr[j] > key` stops shifting as soon as an identical value is encountered, ensuring earlier identical keys remain ahead of later identical keys.
  * **Selection Sort is Unstable:** Long-distance swaps can move an element past an identical counterpart. For example, sorting `[(5, 'A'), (5, 'B'), (1, 'C')]`: the first pass swaps `(5, 'A')` with `(1, 'C')`, yielding `[(1, 'C'), (5, 'B'), (5, 'A')]`. The original order of equal keys 5 is inverted.
* **Adaptivity:**
  * **Insertion Sort is Adaptive:** Runtime scales down smoothly from $\mathcal{O}(n^2)$ to $\mathcal{O}(n)$ as the degree of sortedness increases.
  * **Selection Sort is Non-Adaptive:** Has zero awareness of pre-existing order; always performs exactly $\frac{n(n-1)}{2}$ comparisons.

---

## 4. Empirical Benchmarks & Experimental Results

### 4.1 Experimental Methodology
* **Language & Runtime:** Python 3.9.6 (64-bit)
* **Measurement Metrics:**
  * **CPU Wall-Clock Time:** High-resolution `time.perf_counter()` (millisecond precision).
  * **Peak Auxiliary Memory:** Standard library `tracemalloc` (KiB).
  * **Instruction Instrumentation:** Exact comparison and swap/shift count trackers.
* **Test Configurations:**
  * **Best Case:** Strictly ascending lists `[0, 1, 2, ..., N-1]`
  * **Average Case:** Randomly shuffled permutations (deterministic seed for reproducibility)
  * **Worst Case:** Strictly descending lists `[N, N-1, ..., 1]`
  * **Input Sizes ($N$):** 100, 500, 1000, 2000, 5000

---

### 4.2 CPU Execution Time & Memory Usage

| Scenario | Size ($N$) | Insertion Sort Time (ms) | Selection Sort Time (ms) | Insertion Peak Mem (KiB) | Selection Peak Mem (KiB) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Best Case** | 100 | **0.013** | 0.217 | 0.55 | 0.59 |
| **Best Case** | 500 | **0.211** | 22.483 | 0.16 | 0.25 |
| **Best Case** | 1000 | **0.507** | 105.451 | 0.16 | 0.28 |
| **Best Case** | 2000 | **1.147** | 436.026 | 0.16 | 0.28 |
| **Best Case** | 5000 | **2.921** | 2732.469 | 0.16 | 0.28 |
| **Average Case** | 100 | **0.198** | 0.209 | 0.09 | 0.14 |
| **Average Case** | 500 | **15.345** | 21.825 | 0.16 | 0.25 |
| **Average Case** | 1000 | **89.837** | 105.261 | 0.16 | 0.28 |
| **Average Case** | 2000 | 432.213 | **425.408** | 0.16 | 0.28 |
| **Average Case** | 5000 | 2826.277 | **2686.386** | 0.16 | 0.28 |
| **Worst Case** | 100 | 0.433 | **0.221** | 0.09 | 0.14 |
| **Worst Case** | 500 | 21.836 | **21.860** | 0.16 | 0.25 |
| **Worst Case** | 1000 | 146.476 | **106.734** | 0.16 | 0.28 |
| **Worst Case** | 2000 | 746.686 | **429.621** | 0.16 | 0.28 |
| **Worst Case** | 5000 | 5083.466 | **2752.356** | 0.16 | 0.28 |

---

### 4.3 Operational Metrics: Comparisons vs. Swaps/Shifts

| Scenario | Size ($N$) | Ins. Comparisons | Sel. Comparisons | Ins. Shifts (Writes) | Sel. Swaps (Writes) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Best Case** | 100 | **99** | 4,950 | **0** | 0 |
| **Best Case** | 500 | **499** | 124,750 | **0** | 0 |
| **Best Case** | 1000 | **999** | 499,500 | **0** | 0 |
| **Best Case** | 2000 | **1,999** | 1,999,000 | **0** | 0 |
| **Best Case** | 5000 | **4,999** | 12,497,500 | **0** | 0 |
| **Average Case** | 100 | 2,452 | 4,950 | 2,359 | **95** |
| **Average Case** | 500 | 65,499 | 124,750 | 65,008 | **492** |
| **Average Case** | 1000 | 243,592 | 499,500 | 242,598 | **992** |
| **Average Case** | 2000 | 1,011,386 | 1,999,000 | 1,009,387 | **1,993** |
| **Average Case** | 5000 | **6,220,482** | 12,497,500 | 6,215,491 | **4,991** |
| **Worst Case** | 100 | 4,950 | 4,950 | 4,950 | **50** |
| **Worst Case** | 500 | 124,750 | 124,750 | 124,750 | **250** |
| **Worst Case** | 1000 | 499,500 | 499,500 | 499,500 | **500** |
| **Worst Case** | 2000 | 1,999,000 | 1,999,000 | 1,999,000 | **1,000** |
| **Worst Case** | 5000 | 12,497,500 | 12,497,500 | 12,497,500 | **2,500** |

---

### 4.4 Analysis of Experimental Findings

1. **The Sub-Linear Phenomenon in Best Case:**
   * At $N = 5,000$, Insertion Sort completes in **$2.92\text{ ms}$**, performing only **$4,999$ comparisons**.
   * Selection Sort requires **$2,732.47\text{ ms}$**, performing **$12,497,500$ comparisons**.
   * **Conclusion:** Insertion Sort is **$935.4\times$ faster** when data is already ordered.

2. **The Swap vs. Shift Trade-off in Worst Case:**
   * In the worst case (reverse order), both algorithms execute the identical number of comparisons: $12,497,500$.
   * However, Selection Sort takes **$2,752.36\text{ ms}$**, whereas Insertion Sort takes **$5,083.47\text{ ms}$** (Selection Sort is **$1.85\times$ faster**).
   * **Why?** Insertion Sort performs $12,497,500$ shift writes. Selection Sort performs only $2,500$ array swaps. Memory write operations in Python's list implementation incur significant overhead; reducing writes from $12.5$ million to $2,500$ makes Selection Sort much faster on reverse arrays.

3. **Memory Profile:**
   * Both algorithms exhibit tiny, constant auxiliary memory profiles ($< 0.60\text{ KiB}$), confirming empirical alignment with $\mathcal{O}(1)$ space bounds.

---

## 5. Comparison & Best Use Cases

### 5.1 Comprehensive Comparison Matrix

| Feature | Insertion Sort | Selection Sort |
| :--- | :--- | :--- |
| **Best-Case Time Complexity** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ |
| **Average-Case Time Complexity** | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ |
| **Worst-Case Time Complexity** | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ |
| **Auxiliary Memory (Space)** | $\mathcal{O}(1)$ (In-place) | $\mathcal{O}(1)$ (In-place) |
| **Data Movement (Memory Writes)** | $\mathcal{O}(n^2)$ shifts | $\mathcal{O}(n)$ swaps (at most $n-1$) |
| **Stability** | **Yes** (Stable) | **No** (Unstable in standard form) |
| **Adaptive Behavior** | **Yes** (Scales to $\mathcal{O}(n)$) | **No** (Constant comparisons) |
| **Online Processing** | **Yes** (Can sort streaming data) | **No** (Requires entire list) |

---

### 5.2 When to Choose Insertion Sort

* **Small Datasets ($n \le 50$):** Due to negligible function call overhead and minimal instructions per loop, Insertion Sort consistently outperforms $O(n \log n)$ algorithms (like QuickSort and MergeSort) on small inputs.
* **Nearly-Sorted or Partially Sorted Data:** When adding a batch of new elements to an already sorted database or list, Insertion Sort runs in near-linear $\mathcal{O}(n + d)$ time, where $d$ is the number of inversions.
* **Online / Streaming Data:** Insertion Sort can insert incoming elements into their proper place on-the-fly as they arrive from a network socket or user input stream.
* **Hybrid Industrial Sorting Algorithms:**
  * **TimSort (Python's `sorted()` and Java's `Arrays.sort()`):** Uses Insertion Sort for runs with length under 32 or 64.
  * **Introsort (C++ `std::sort`):** Switches to Insertion Sort once QuickSort partitions drop below 16 elements.

---

### 5.3 When to Choose Selection Sort

* **Write-Sensitive Hardware (Flash Memory & EEPROM):**  
  In embedded systems and microcontrollers (e.g., IoT sensors logging to flash storage), memory write cycles deteriorate hardware life and consume substantial battery power. Selection Sort guarantees at most $n-1$ write operations ($\mathcal{O}(n)$), compared to up to $n^2/2$ writes in Insertion Sort.
* **Strict Auxiliary Memory Limits:** Where data must be sorted strictly in-place with no recursive stack frames (unlike QuickSort/MergeSort) and stability is not required.
* **Reverse-Dominant Unsorted Batches:** When inputs are predominantly inverted and write latency exceeds comparison cost.

---

## 6. Project Structure & Execution Guide

### Repository Structure
```
├── README.md               # Main Project Report (this file)
├── insertion_sort.py       # Standalone implementation with docstrings & metrics
├── selection_sort.py       # Standalone implementation with docstrings & metrics
├── benchmark.py            # Automated CPU & memory profiling suite
├── tests.py                # Correctness, edge cases & stability test suite
└── PRESENTATION_NOTES.md   # Oral exam preparation & defense guide
```

### How to Run the Code

1. **Verify Correctness & Stability via Unit Tests:**
   ```bash
   python3 tests.py
   ```
   *Expected Output:* `Ran 3 tests in 0.000s ... OK`

2. **Execute Standalone Sorting Implementations:**
   ```bash
   python3 insertion_sort.py
   python3 selection_sort.py
   ```

3. **Reproduce Benchmark Experiments:**
   ```bash
   python3 benchmark.py
   ```

---

## 7. AI Utilization Rules and Ethic Codes

In compliance with the course ethical code of conduct, the following declaration is formally provided:

> “Gemini 3.8 Flash was used in the Code generation, Algorithmic profiling, and Report documentation sections of this product. The tool was utilized via the prompt/input "use python , insertion sort vs selection sort , and my name is saifuddin sayyaf 2422190016" for the purpose of Code generation / Algorithm editing / Documentation / Text correction. The output generated has been reviewed and verified by me for technical accuracy, safety, and originality. I bear full responsibility for the work.”

**Student Name:** Saifuddin Sayyaf  
**Student ID:** 2422190016  
**Signature:** *Saifuddin Sayyaf*  
**Date:** 21.10.2026
