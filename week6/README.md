# Week 6 - Binary Trees (LeetCode lab)

All solutions are written in Python. Each folder has `solution.py` (code + small tests) and `README.md` (report).

To run the tests of one problem:

```
python 01_binary_tree_inorder_traversal/solution.py
```

| # | Problem | Time | Space |
|---|---------|------|-------|
| 1 | [94. Binary Tree Inorder Traversal](01_binary_tree_inorder_traversal) | O(n) | O(h) |
| 2 | [104. Maximum Depth of Binary Tree](02_maximum_depth_of_binary_tree) | O(n) | O(h) |
| 3 | [111. Minimum Depth of Binary Tree](03_minimum_depth_of_binary_tree) | O(n) | O(h) |
| 4 | [112. Path Sum](04_path_sum) | O(n) | O(h) |
| 5 | [144. Binary Tree Preorder Traversal](05_binary_tree_preorder_traversal) | O(n) | O(h) |
| 6 | [145. Binary Tree Postorder Traversal](06_binary_tree_postorder_traversal) | O(n) | O(h) |
| 7 | [226. Invert Binary Tree](07_invert_binary_tree) | O(n) | O(h) |
| 8 | [257. Binary Tree Paths](08_binary_tree_paths) | O(n * h) | O(h^2) |
| 9 | [404. Sum of Left Leaves](09_sum_of_left_leaves) | O(n) | O(h) |
| 10 | [617. Merge Two Binary Trees](10_merge_two_binary_trees) | O(min(n, m)) | O(min(h1, h2)) |

n = number of nodes, h = height of the tree (log n if balanced, n in the worst case when the tree is like a line).

## What I noticed this week

- Almost every problem here is the same idea: do something with the node, and call the same function
  for the left and right child. The difference is only **what** you do and **when** (before, between or after the calls).
- The most common mistake I made was mixing up "node is `None`" and "node is a leaf". In Minimum Depth,
  Path Sum and Binary Tree Paths this gave wrong answers for nodes that have only one child.
- Recursion uses memory for the call stack, so space is O(h), not O(1), even when I don't create any lists.
