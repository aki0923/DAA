# 617. Merge Two Binary Trees

Link: https://leetcode.com/problems/merge-two-binary-trees/

Code: [solution.py](solution.py)

## 1. Problem

We have two trees. We put one on top of the other. Where both trees have a node in the same place,
the new node has the sum of the two values. Where only one tree has a node, we just take that node.
Return the new merged tree.

## 2. Approach

Recursion that walks both trees at the same time:

1. If `root1` is `None` -> return `root2` (whatever it is, even `None`).
2. If `root2` is `None` -> return `root1`.
3. Both exist -> make a new node with `root1.val + root2.val`.
4. Its left child = merge of both left children, its right child = merge of both right children.

Important thing: when one side is `None`, I don't go deeper. I just attach the whole subtree from the other tree.

### Tracing

Example: `root1 = [1, 3, 2, 5]`, `root2 = [2, 1, 3, null, 4, null, 7]`

```
root1:        root2:          result:
     1             2               3
    / \           / \             / \
   3   2         1   3           4   5
  /               \   \         / \   \
 5                 4   7       5   4   7
```

| Call merge(a, b) | case | result |
|------------------|------|--------|
| merge(1, 2) | both exist | new node 3, now go to children |
| merge(3, 1) (left) | both exist | new node 4 |
| merge(5, None) | root2 is None | take node 5 from root1 |
| merge(None, 4) | root1 is None | take node 4 from root2 |
| merge(2, 3) (right) | both exist | new node 5 |
| merge(None, None) | root1 is None | return None |
| merge(None, 7) | root1 is None | take node 7 |

Result as list: `[3, 4, 5, 5, 4, null, 7]` - correct.

### Challenges / what did not work

- My first version had only one check: `if root1 is None and root2 is None: return None`.
  Then for `merge(5, None)` it tried to do `root1.val + root2.val` and crashed with
  `AttributeError: 'NoneType' object has no attribute 'val'`. I needed separate checks for each tree.
- After fixing that, I wrote code that, when one node is `None`, still made new nodes and treated the missing
  value as 0, and went down to the very end of the bigger tree. It worked, but it was doing extra work for nothing.
  Then I understood that I can just return the existing subtree, because there is nothing to add to it.
- Note: my solution reuses some nodes from the input trees (the parts where only one tree had nodes).
  So the result is connected to the original trees. LeetCode accepts it, but if I change the result later,
  the input tree changes too. I wrote this down so I remember it.

### Testing

LeetCode examples, both trees empty, one empty and one not, and the opposite case.

## 3. Time and Space Complexity

**Time Complexity: O(min(n, m))**, n and m = number of nodes in the two trees.
We only do real work (making a new node and going deeper) in places where **both** trees have a node.
As soon as one side is `None`, we return immediately and attach the other subtree without visiting it.
The number of places where both trees have a node is not more than the size of the smaller tree.

**Space Complexity: O(min(h1, h2))** for the recursion stack - we only go deep while both trees continue.
Worst case O(n) if both trees are lines. Also we create O(min(n, m)) new nodes for the overlapping part.

## 4. Reflection / Improvement

- I think time can't be better than O(min(n, m)), because every overlapping pair of nodes has to be summed.
- To save memory I could write the sums directly into `root1` (`root1.val += root2.val`) instead of making new
  nodes. Then extra memory is only the recursion stack. But it changes the input tree, which is not always ok.
- An iterative version with a stack of pairs `(node1, node2)` would avoid deep recursion, same complexity.
