# 108. Convert Sorted Array to Binary Search Tree

## 1. Problem

We have an array of numbers sorted from small to big. We need to make a binary search tree from it, and the tree must be height-balanced. Height-balanced means that for every node the heights of left and right subtrees differ by not more than 1.

## 2. Approach

The main idea: the middle element of the array should be the root. Then half of the numbers go to the left (they are smaller) and half go to the right (they are bigger), so the tree is balanced.

Steps:
1. If array is empty -> return `None`.
2. Take `mid = len(nums) // 2`.
3. Make a node with `nums[mid]`.
4. Left child = do the same for `nums[:mid]` (left part).
5. Right child = do the same for `nums[mid+1:]` (right part).
6. Return the node.

### Tracing

**Example 1:** `nums = [-10, -3, 0, 5, 9]`

| Call | Array | mid | Node | Left part | Right part |
|------|-------|-----|------|-----------|------------|
| 1 | [-10, -3, 0, 5, 9] | 2 | 0 | [-10, -3] | [5, 9] |
| 2 | [-10, -3] | 1 | -3 | [-10] | [] |
| 3 | [-10] | 0 | -10 | [] | [] |
| 4 | [5, 9] | 1 | 9 | [5] | [] |
| 5 | [5] | 0 | 5 | [] | [] |

Result:
```
        0
       / \
     -3   9
     /   /
   -10  5
```
Output: `[0, -3, 9, -10, null, 5]` (same as LeetCode example)

**Example 2:** `nums = [1, 2, 3, 4, 5, 6, 7]`

- mid = 3 -> root 4, left [1,2,3], right [5,6,7]
- [1,2,3]: mid = 1 -> 2, left [1], right [3]
- [5,6,7]: mid = 1 -> 6, left [5], right [7]

```
          4
        /   \
       2     6
      / \   / \
     1   3 5   7
```
Perfect tree, height 3.

### Challenges

- My first idea was to take numbers one by one and insert them into a BST with normal insert. But the array is sorted, so every new number is bigger and goes to the right. The tree became like a linked list: 1 -> 2 -> 3 -> 4 ... This is a valid BST but **not balanced**, so the answer is wrong. Also insert takes O(n) each time so it was O(n²).
- Then I understood that the root must be the middle element, and the same for every subtree.
- I had a problem with slices: I wrote `nums[mid:]` for the right part instead of `nums[mid + 1:]`. The middle element was included again and the recursion never finished (for array of 1 element mid = 0 and `nums[0:]` is the same array) -> `RecursionError`.
- For even length there are two middles. I take `len // 2` (the right one). LeetCode accepts any balanced answer so it is fine.

### Testing

In `solution.py` I check every result in two ways:
1. Inorder traversal of the tree must give back the same sorted array (this means it is a correct BST).
2. A function `is_balanced` checks heights of left and right for every node.

Tested with odd length, even length, 1 element. All passed.

## 3. Time Complexity

**Time Complexity: O(n log n)**

The recursion itself creates every node one time, that would be O(n). But I use slicing (`nums[:mid]` and `nums[mid+1:]`) and in Python slicing **copies** the elements. On each level of recursion all slices together have about n elements, so each level costs O(n) for copying. The array is divided by 2 each time, so there are log n levels. Together: O(n) * log n = O(n log n).

**Space Complexity: O(n)**

- The tree itself has n nodes -> O(n).
- The recursion depth is log n because array is split in half.
- The slices: at one moment we keep slices only on the current path, sizes n/2 + n/4 + n/8 + ... which is less than n -> O(n).

So total O(n).

## 4. Reflection / Improvement

- **Is there a more efficient approach?** Yes. The slow part is copying the array with slices.
- **What would you need to change?** Don't make new arrays, pass two indexes `left` and `right` into a helper function and work on the same array:
  ```python
  def helper(left, right):
      if left > right:
          return None
      mid = (left + right) // 2
      node = TreeNode(nums[mid])
      node.left = helper(left, mid - 1)
      node.right = helper(mid + 1, right)
      return node
  ```
- **What complexity could the improved solution achieve?** Time **O(n)**, because every element is used only once and nothing is copied. Extra space **O(log n)** for the recursion stack (plus O(n) for the tree we must return anyway).
