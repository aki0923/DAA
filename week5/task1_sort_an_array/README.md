# Task 1: Sort an Array

## 1. Problem
The task requires sorting an array of integers in ascending order without using built-in sorting functions (e.g., `sort()` or `sorted()`).

## 2. Approach
I implemented the **Merge Sort** algorithm, which works on the Divide-and-Conquer strategy:
1. **Divide**: Recursively split the array into two equal (or nearly equal) halves until each subarray contains only one element.
2. **Conquer**: A subarray of size 1 is inherently sorted.
3. **Combine**: Merge the smaller sorted arrays into a larger sorted array by comparing their smallest remaining elements.

### Step-by-Step Tracing Example
Input array: `[5, 2, 3, 1]`

1. **Splitting phase**:
   - `[5, 2, 3, 1]` → Left: `[5, 2]`, Right: `[3, 1]`
   - Left `[5, 2]` → Split into `[5]` and `[2]`
   - Right `[3, 1]` → Split into `[3]` and `[1]`

2. **Merging phase**:
   - Merge `[5]` and `[2]`: compare 5 and 2 → Result: `[2, 5]`
   - Merge `[3]` and `[1]`: compare 3 and 1 → Result: `[1, 3]`
   - Merge `[2, 5]` and `[1, 3]`:
     - Compare 2 and 1 → Add 1 (`[1]`)
     - Compare 2 and 3 → Add 2 (`[1, 2]`)
     - Compare 5 and 3 → Add 3 (`[1, 2, 3]`)
     - Append remaining element 5 → Result: `[1, 2, 3, 5]`

### Challenges Faced
* **Initial Attempt**: I first considered using Insertion Sort or Bubble Sort due to their simplicity. However, their $O(n^2)$ time complexity results in a Time Limit Exceeded (TLE) status on LeetCode for large inputs ($N = 50,000$).
* **Memory Handling**: Creating sliced subarrays (`arr[:mid]`) in Python generates extra space overhead. Implementing Merge Sort requires carefully handling memory allocations to avoid excessive space allocation.

## 3. Time & Space Complexity

### Time Complexity: $O(n \log n)$
- **Splitting**: The array is divided in half recursively, creating a recursion tree of height $\log_2 n$.
- **Merging**: At each of the $\log n$ levels, we perform a linear scan ($O(n)$ steps) to merge all elements.
- Overall time complexity is $O(n \log n)$ across all cases (Best, Average, Worst).

### Space Complexity: $O(n)$
- Auxiliary memory is required to store the temporary arrays during the merge operation and for the recursive call stack.

## 4. Reflection / Improvement
* **Can it be improved?** Yes, in terms of memory usage.
* **Modification**: We can use **Quick Sort** (with randomized pivot choice) or **Heap Sort** to achieve $O(1)$ auxiliary space complexity while maintaining an average $O(n \log n)$ time complexity.
* **Timsort**: Python’s standard `sorted()` uses Timsort, which takes advantage of already ordered segments (runs) in real-world data to achieve up to $O(n)$ best-case time complexity.