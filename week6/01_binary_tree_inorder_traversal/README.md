# 94. Binary Tree Inorder Traversal

Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

Code: [solution.py](solution.py)

## 1. Problem

We get the root of a binary tree and we need to return the values of all nodes in "inorder" order.
Inorder means: first visit the left subtree, then the node itself, then the right subtree.

## 2. Approach

I used recursion with a helper function `dfs(node)`:

1. If the node is `None` - just return, nothing to do.
2. Call `dfs` for the left child.
3. Add `node.val` to the result list.
4. Call `dfs` for the right child.

The result list is created one time outside the helper, and every call adds to the same list.

### Tracing

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
| 1 | dfs(1) | go left -> dfs(None), returns right away | [] |
| 2 | dfs(1) | add 1 | [1] |
| 3 | dfs(1) | go right -> dfs(2) | [1] |
| 4 | dfs(2) | go left -> dfs(3) | [1] |
| 5 | dfs(3) | left is None, add 3 | [1, 3] |
| 6 | dfs(3) | right is None, go back to dfs(2) | [1, 3] |
| 7 | dfs(2) | add 2 | [1, 3, 2] |
| 8 | dfs(2) | right is None, everything is finished | [1, 3, 2] |

Answer: `[1, 3, 2]` - correct.

### Challenges / what did not work

- My first version returned lists and joined them:
  `return inorder(root.left) + [root.val] + inorder(root.right)`.
  It passed, but then I understood that `+` makes a new list every time and copies all elements.
  For a tree that looks like a line (every node has only one child) this copying becomes about n^2 operations.
  So I changed it to one shared list and `append`.
- LeetCode asks to try it without recursion. In my first iterative try I popped the node right after pushing it,
  and I got preorder `[1, 2, 3]` instead of inorder. The fix was: first go left as far as possible and push all nodes
  to the stack, and only after that pop one node, add it, and move to its right child.
  I kept both versions in the code (`inorderTraversalIterative`).

### Testing

I tested with the examples from LeetCode, an empty tree, a tree with one node and a bigger tree.
Both versions (recursive and iterative) give the same answers.

## 3. Time and Space Complexity

**Time Complexity: O(n)**, n = number of nodes.
Every node is visited exactly one time, and for every node we do a constant amount of work
(one append and two calls). So the total is about n steps.

**Space Complexity: O(h)** extra, h = height of the tree.
This is the recursion stack (or my own stack in the iterative version). If the tree is balanced, h is about log n.
If the tree is like a line, h = n, so the worst case is O(n). The result list is also O(n) but we need it for the answer anyway.

## 4. Reflection / Improvement

- Time cannot be better than O(n), because we have to return all n values.
- The space can be improved with **Morris traversal**. It temporarily connects the rightmost node of the left subtree
  back to the current node, so we don't need a stack. Extra space becomes **O(1)**. It is harder to write and it
  changes the tree for a while (then fixes it back), so I did not implement it.
