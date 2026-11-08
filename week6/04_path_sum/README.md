# 112. Path Sum

Link: https://leetcode.com/problems/path-sum/

Code: [solution.py](solution.py)

## 1. Problem

We get a tree and a number `targetSum`. We need to say `True` if there is a path from the root down to a **leaf**
where the sum of all values on the path equals `targetSum`. Otherwise `False`.

## 2. Approach

Instead of adding values on the way down, I subtract them from the target.

1. If node is `None` -> `False`.
2. `remaining = targetSum - node.val`.
3. If node is a leaf -> return `remaining == 0`.
4. Otherwise, check the left subtree with `remaining`, and if it didn't work, check the right subtree.

So every call just asks: "can I make `remaining` from here down to some leaf?"

### Tracing

Example: `root = [5,4,8,11,null,13,4,7,2,null,null,null,1]`, `targetSum = 22`

```
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1
```

| Node | remaining after subtracting | leaf? | result |
|------|---------------------------|-------|--------|
| 5 | 22 - 5 = 17 | no | go left |
| 4 | 17 - 4 = 13 | no | go left |
| 11 | 13 - 11 = 2 | no | go left |
| 7 | 2 - 7 = -5 | yes | -5 != 0 -> False, go back |
| 2 | 2 - 2 = 0 | yes | 0 == 0 -> **True** |

Because of `or`, as soon as node 2 returns `True`, all calls above return `True` too and the right side (8, 13, 4, 1)
is not checked at all. Path: 5 -> 4 -> 11 -> 2 = 22.

### Challenges / what did not work

- My first version checked the answer when I reach `None`:
  ```python
  if root is None:
      return targetSum == 0
  ```
  It looked shorter, but it is wrong. Test `root = [1, 2]`, `targetSum = 1`:
  the root 1 has no right child, so going right I get `None` with remaining 0 and the code says `True`.
  But node 1 is not a leaf (it has child 2), so the path `[1]` doesn't count. The answer must be `False`.
  So I moved the check to the moment when the node is a real leaf.
- I also had a question if I can stop early when `remaining < 0`. No, because values can be negative
  (test `[-2, null, -3]`, target -5 -> True). So I can't cut the search like that.

### Testing

LeetCode examples, empty tree, the `[1, 2]` case from above, and a test with negative numbers.

## 3. Time and Space Complexity

**Time Complexity: O(n)**.
In the worst case (no such path) we visit every node one time, and in each node we do one subtraction and one comparison.

**Space Complexity: O(h)**, h = height of the tree, for the recursion stack.
Balanced: O(log n), worst case (line): O(n).

## 4. Reflection / Improvement

- I don't think time can be better than O(n) in the worst case: if the answer is `False`, we have to check
  every root-to-leaf path, which means every node.
- We could write it with a stack (iterative DFS) storing pairs `(node, remaining)`. Complexity stays the same,
  but there is no Python recursion limit problem for very deep trees.
- My solution already stops early when it finds the path (because of `or`), which helps when the answer is `True`.
