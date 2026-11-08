# 145. Binary Tree Postorder Traversal

Link: https://leetcode.com/problems/binary-tree-postorder-traversal/

Code: [solution.py](solution.py)

## 1. Problem

Return the values of the tree in "postorder" order: first the left subtree, then the right subtree,
and the node itself goes **last**.

## 2. Approach

Recursive version - same as the other traversals, only the `append` is at the end:

1. If node is `None` -> return.
2. `dfs(left)`.
3. `dfs(right)`.
4. Add `node.val`.

Stack version - I found a small trick while I was drawing:
- Preorder with a stack gives "node, left, right".
- If I change the order of pushing, I get "node, right, left".
- If I reverse "node, right, left", I get "left, right, node" - and this is exactly postorder.

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
| 1 | dfs(1) | left is None, go right -> dfs(2) | [] |
| 2 | dfs(2) | go left -> dfs(3) | [] |
| 3 | dfs(3) | no children, add 3 | [3] |
| 4 | dfs(2) | right is None, add 2 | [3, 2] |
| 5 | dfs(1) | both sides done, add 1 | [3, 2, 1] |

Answer: `[3, 2, 1]`.

### Tracing (stack version), same tree

| Step | stack before | pop | push | result |
|------|-------------|-----|------|--------|
| 1 | [1] | 1 | 2 | [1] |
| 2 | [2] | 2 | 3 | [1, 2] |
| 3 | [3] | 3 | - | [1, 2, 3] |

Reverse `[1, 2, 3]` -> `[3, 2, 1]`. Correct.

### Challenges / what did not work

- I tried to write a "real" iterative postorder without reversing. The problem is that when I pop a node
  I don't know if I already visited its right child or not. I tried to add a `visited` set and it became messy
  and I had bugs where nodes were added twice. Then I found the reverse trick by comparing it to preorder,
  and it was much simpler.
- One more mistake: in the reverse trick I first pushed right then left (like in preorder) and got
  on the tree `[1, 2, 3]` I got `[3, 2, 1]` instead of `[2, 3, 1]`. In this version I need to push **left first**,
  so that right is popped first.

### Testing

LeetCode examples, empty tree, one node, bigger tree. Both versions give the same results.

## 3. Time and Space Complexity

**Time Complexity: O(n)**.
Recursive: one call per node. Stack version: every node is pushed and popped one time, plus `reverse()` which is
also O(n). O(n) + O(n) is still O(n).

**Space Complexity:**
- Recursive: **O(h)** for the call stack (O(log n) balanced, O(n) worst case).
- Stack version: the stack can hold up to O(n) nodes in the worst case, plus the result list O(n).

## 4. Reflection / Improvement

- Time can't be better than O(n).
- The reverse trick is easy, but it is not a "true" postorder while walking (we only get the right order at the end).
  A version with one stack and a `last_visited` pointer gives real postorder order with O(h) space.
- Morris traversal can make extra space **O(1)**, but for postorder it is the most complicated one, so I didn't do it.
