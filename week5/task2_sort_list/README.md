# Task 2: Sort List

## 1. Problem
Given the `head` of a singly linked list, return the list after sorting it in ascending order. The optimal time complexity requirement is $O(n \log n)$ with $O(1)$ or $O(\log n)$ memory.

## 2. Approach
Merge Sort is ideally suited for Linked Lists because elements do not require contiguous memory indexing, and pointers can be re-linked efficiently without creating new nodes.

1. **Find Middle**: Use the Fast & Slow Pointer technique (Tortoise and Hare) to locate the midpoint of the linked list.
2. **Disconnect**: Break the linked list into two independent halves by setting `slow.next = None`.
3. **Recursive Sort**: Recursively call `sortList` on both halves.
4. **Merge**: Merge the two sorted linked lists using a standard two-pointer list merge technique with a dummy node.

### Step-by-Step Tracing Example
Input List: `4 -> 2 -> 1 -> 3`

1. **Split phase**:
   - Fast/Slow pointers locate mid at node `2`.
   - Disconnect list into `4 -> 2` and `1 -> 3`.
   - Subdivide `4 -> 2` into `4` and `2`.
   - Subdivide `1 -> 3` into `1` and `3`.

2. **Merge phase**:
   - Merge `4` and `2`: Node `2` linked to Node `4` $\rightarrow$ `2 -> 4`.
   - Merge `1` and `3`: Node `1` linked to Node `3` $\rightarrow$ `1 -> 3`.
   - Merge `2 -> 4` and `1 -> 3`:
     - Compare 2 and 1 $\rightarrow$ append 1
     - Compare 2 and 3 $\rightarrow$ append 2
     - Compare 4 and 3 $\rightarrow$ append 3
     - Append remaining 4 $\rightarrow$ `1 -> 2 -> 3 -> 4`.

### Challenges Faced
* **Infinite Loops during Split**: Finding the midpoint of an even-length list required initializing `fast = head.next` instead of `head`. Otherwise, `slow` ends up at the last element during a 2-node list split, resulting in infinite recursive calls.
* **Pointer Management**: Ensuring the original link between the left half and right half is properly severed (`slow.next = None`) before recursion.

## 3. Time & Space Complexity

### Time Complexity: $O(n \log n)$
- Finding the middle node takes $O(n)$ time per division level.
- Splitting takes $\log n$ recursive levels.
- Merging $n$ node links at each level takes $O(n)$ time.
- Total time complexity: $O(n \log n)$.

### Space Complexity: $O(\log n)$
- The recursive call stack takes $O(\log n)$ stack frames corresponding to the height of the recursion tree.

## 4. Reflection / Improvement
* **Can it be improved?** Yes, the space complexity can be reduced from $O(\log n)$ down to strictly $O(1)$.
* **Modification**: An iterative bottom-up Merge Sort can be implemented instead of top-down recursion. By merging sublists of size 1, 2, 4, 8, etc., in an iterative loop, no recursive stack space is required.
* **Complexity of Improved Solution**:
  - Time Complexity: $O(n \log n)$
  - Space Complexity: $O(1)$