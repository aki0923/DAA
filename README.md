# 700. Search in a Binary Search Tree

## 1. Problem

We have the root of a binary search tree and a number `val`. We need to find the node that has this value and return it (so we return the whole subtree that starts from this node). If there is no such node we return `null` (`None` in Python).

## 2. Approach

In a BST everything on the left of a node is smaller and everything on the right is bigger. So I don't need to check the whole tree, I can just go one direction every time.

My steps:
1. If the node is `None` -> the value is not in the tree, return `None`.
2. If `node.val == val` -> found it, return the node.
3. If `val < node.val` -> call the function again for the left child.
4. Else -> call the function again for the right child.

I used recursion because it was easier for me to write.

### Tracing

Tree:
```
        4
       / \
      2   7
     / \
    1   3
```

**Example 1: val = 2**

| Step | Current node | Compare | Action |
|------|--------------|---------|--------|
| 1 | 4 | 2 < 4 | go left |
| 2 | 2 | 2 == 2 | found, return node 2 |

Result: subtree `[2, 1, 3]`

**Example 2: val = 5**

| Step | Current node | Compare | Action |
|------|--------------|---------|--------|
| 1 | 4 | 5 > 4 | go right |
| 2 | 7 | 5 < 7 | go left |
| 3 | None | - | not found, return None |

Result: `[]`

Only 2-3 nodes were checked, not all 5.

### Challenges

- My first idea was to just do normal DFS and check left and right subtree both, like in a normal binary tree. It worked, but then I understood that I'm not using the BST property at all and it checks every node, so it is O(n) always. Then I changed it to go only to one side.
- At first I forgot the `return` before the recursive calls (`self.searchBST(root.left, val)` without return). Because of this the function returned `None` even when the value was in the tree. It took some time to find this bug.
- I also forgot the case when root is `None` at the start (empty tree), the program crashed with `AttributeError`. Added the check in the beginning.

### Testing

I built the tree manually in `solution.py` and tested: value in the middle (2), value not in tree (5), leaf (7) and empty tree. All gave correct output.

## 3. Time Complexity

**Time Complexity: O(h)**, where h is the height of the tree.

Each step I go one level down and I never come back up, so the maximum number of steps is the height of the tree.
- If the tree is balanced, h = log n, so it is **O(log n)**.
- If the tree is very unbalanced (like a linked list, for example 1 -> 2 -> 3 -> 4 all to the right), h = n, so worst case is **O(n)**.

**Space Complexity: O(h)**

Because of recursion. Every call is saved in the call stack until it returns, and there can be h calls at the same time. Balanced tree O(log n), worst case O(n).

## 4. Reflection / Improvement

- **Is there a more efficient approach?** For time no, we have to go down the tree anyway, O(h) is the best for a normal BST. But memory can be better.
- **What would you need to change?** Use a `while` loop instead of recursion:
  ```python
  while root != None and root.val != val:
      if val < root.val:
          root = root.left
      else:
          root = root.right
  return root
  ```
- **What complexity could the improved solution achieve?** Time still O(h), but space becomes **O(1)** because there is no call stack.
