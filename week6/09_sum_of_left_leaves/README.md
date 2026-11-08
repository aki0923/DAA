# 404. Sum of Left Leaves

Link: https://leetcode.com/problems/sum-of-left-leaves/

Code: [solution.py](solution.py)

## 1. Problem

Find the sum of all leaves that are **left** children of their parent.
So a node counts only if two things are true: it has no children, and it is on the left side of its parent.

## 2. Approach

The problem is that a node itself doesn't know if it is a left or a right child. So I pass this information
from the parent as a flag `is_left`.

`dfs(node, is_left)`:
1. If node is `None` -> 0.
2. If node is a leaf -> return `node.val` if `is_left` is `True`, otherwise 0.
3. Otherwise return `dfs(left, True) + dfs(right, False)`.

For the root I call `dfs(root, False)`, because the root has no parent.

### Tracing

Example: `root = [3, 9, 20, null, null, 15, 7]`

```
      3
     / \
    9   20
       /  \
      15   7
```

| Call | leaf? | is_left | returns |
|------|-------|---------|---------|
| dfs(3, False) | no | - | dfs(9, True) + dfs(20, False) |
| dfs(9, True) | yes | True | 9 |
| dfs(20, False) | no | - | dfs(15, True) + dfs(7, False) |
| dfs(15, True) | yes | True | 15 |
| dfs(7, False) | yes | False | 0 |
| back in dfs(20) | | | 15 + 0 = 15 |
| back in dfs(3) | | | 9 + 15 = **24** |

Answer: 24.

### Challenges / what did not work

- My first idea was "sum of all left children". On the LeetCode example it gave the correct 24 by luck,
  because there both left children (9 and 15) are leaves. But on `[1, 2, 3, 4, 5]`:
  ```
        1
       / \
      2   3
     / \
    4   5
  ```
  it gave 2 + 4 = 6. The correct answer is **4**, because 2 is not a leaf. So I added the leaf check.
- Another case I almost missed: tree with one node `[1]`. The root is a leaf, but it is not a left child,
  so the answer is 0, not 1. That's why the first call uses `is_left = False`.
- I also thought about checking from the parent: "if `node.left` exists and `node.left` has no children,
  add `node.left.val`". This also works and doesn't need a flag, but the flag version was easier for me to read.

### Testing

LeetCode examples, `[1]`, `[1, 2, 3, 4, 5]`, empty tree, and `[1, null, 2, 3]` where the left leaf is deep
in the right subtree (answer 3).

## 3. Time and Space Complexity

**Time Complexity: O(n)**.
Each node is visited one time, and in each node we do only a few checks and one addition.

**Space Complexity: O(h)** for the recursion stack, h = height of the tree.
Balanced: O(log n), worst case (line): O(n).

## 4. Reflection / Improvement

- O(n) time is needed: we can't know where the left leaves are without looking at every node.
- It can be done with BFS or with a stack where I store `(node, is_left)` pairs. The complexity is the same,
  but it avoids deep recursion. With Morris traversal extra space could be O(1), but that is too complicated
  for this problem.
