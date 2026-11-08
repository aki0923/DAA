# 226. Invert Binary Tree

Link: https://leetcode.com/problems/invert-binary-tree/

Code: [solution.py](solution.py)

## 1. Problem

We need to make a "mirror" of the tree: for every node, the left child becomes the right child and the right child
becomes the left one. Then return the root.

## 2. Approach

For every node:

1. If the node is `None` -> return `None`.
2. Save the old left child in `temp`.
3. New left = inverted old right subtree.
4. New right = inverted old left subtree (`temp`).
5. Return the node.

So the swap happens in every node, from the top to the bottom, and the recursion makes sure that the subtrees
inside are also mirrored.

### Tracing

Example: `root = [4, 2, 7, 1, 3, 6, 9]`

```
Before:            After:
      4                 4
    /   \             /   \
   2     7           7     2
  / \   / \         / \   / \
 1   3 6   9       9   6 3   1
```

| Call | what happens |
|------|-------------|
| invert(4) | temp = 2. left = invert(7) |
| invert(7) | temp = 6. left = invert(9) -> 9 (leaf, children None). right = invert(6) -> 6. Now 7 has 9 on left, 6 on right |
| back in invert(4) | left = 7 (already mirrored). right = invert(2) |
| invert(2) | temp = 1. left = invert(3) -> 3. right = invert(1) -> 1. Now 2 has 3 on left, 1 on right |
| back in invert(4) | right = 2. return 4 |

Result as a list: `[4, 7, 2, 9, 6, 3, 1]` - correct.

### Challenges / what did not work

- My first version was:
  ```python
  root.left = self.invertTree(root.right)
  root.right = self.invertTree(root.left)
  ```
  On `[2, 1, 3]` I got `[2, 3, 3]`. The problem: in the first line I already overwrote `root.left`,
  so in the second line `root.left` is not the old left child anymore, it is the new one (3).
  The old left subtree (1) was lost. The fix was to save it in `temp` first.
  (In Python you can also do it in one line: `root.left, root.right = invert(root.right), invert(root.left)`,
  because the right side is calculated before assigning.)
- To check answers I had to write `tree_to_list` that turns the tree back into the LeetCode list format,
  otherwise I couldn't compare the result easily.

### Testing

LeetCode examples, empty tree, and `[1, 2]` (only left child -> after inverting only right child: `[1, null, 2]`).

## 3. Time and Space Complexity

**Time Complexity: O(n)**.
Every node is visited one time and the swap itself is constant work.

**Space Complexity: O(h)** for the recursion stack, h = height.
Balanced: O(log n). Worst case (line): O(n). We don't make new nodes, we change the tree in place.

## 4. Reflection / Improvement

- O(n) is the best we can do, because every node has to be swapped.
- It can be done with BFS (queue) or a stack: take a node, swap its children, add the children to the queue.
  Same O(n) time, and no recursion depth problem for very deep trees. Space would be O(width) for BFS.
