# 144. Binary Tree Preorder Traversal

Link: https://leetcode.com/problems/binary-tree-preorder-traversal/

Code: [solution.py](solution.py)

## 1. Problem

Return the values of the tree in "preorder" order: first the node itself, then everything in the left subtree,
then everything in the right subtree.

## 2. Approach

It is almost the same as inorder (problem 94), I only moved the `append` line to the top:

1. If node is `None` -> return.
2. Add `node.val` to the result.
3. `dfs(left)`.
4. `dfs(right)`.

I also wrote a version with a stack:
- Put the root in the stack.
- While the stack is not empty: pop a node, add its value, push the **right** child, then push the **left** child.
- Because a stack is "last in, first out", the left child is popped first, which is what preorder needs.

### Tracing (recursive)

Example: `root = [1, null, 2, 3]`

```
    1
     \
      2
     /
    3
```

| Step | Where I am | What happens | result |
|------|-----------|--------------|--------|
| 1 | dfs(1) | add 1 | [1] |
| 2 | dfs(1) | left is None, go right -> dfs(2) | [1] |
| 3 | dfs(2) | add 2 | [1, 2] |
| 4 | dfs(2) | go left -> dfs(3) | [1, 2] |
| 5 | dfs(3) | add 3, no children | [1, 2, 3] |

Answer: `[1, 2, 3]`.

### Tracing (stack version), same tree

| Step | stack before | pop | push | result |
|------|-------------|-----|------|--------|
| 1 | [1] | 1 | 2 (right) | [1] |
| 2 | [2] | 2 | 3 (left) | [1, 2] |
| 3 | [3] | 3 | nothing | [1, 2, 3] |

### Challenges / what did not work

- In the stack version I first pushed the left child before the right child (it felt natural to write left first).
  On the tree `[1, 2, 3]` I got `[1, 3, 2]` - the right side came out first. I drew the stack on paper and saw that
  the last thing pushed is the first thing popped, so I need to push right first.
- The recursive version had no real problems because I already did inorder before.

### Testing

LeetCode examples, empty tree, one node and one bigger tree. Both versions give the same output.

## 3. Time and Space Complexity

**Time Complexity: O(n)**.
Each node is added to the result exactly once and each node is pushed/popped (or called) exactly once.

**Space Complexity: O(h)** for the recursion, h = height (O(log n) balanced, O(n) for a line).
For the stack version it is also O(h) in the worst case. The result list is O(n), but that is the answer itself.

## 4. Reflection / Improvement

- O(n) time is the best possible, because we output n values.
- Extra space can be made **O(1)** with Morris traversal (the same idea as in inorder, but we add the value at a
  different moment). I didn't implement it because it is much harder to read.
