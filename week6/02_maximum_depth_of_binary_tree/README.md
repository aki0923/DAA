# 104. Maximum Depth of Binary Tree

Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Code: [solution.py](solution.py)

## 1. Problem

We need to find how many nodes are on the longest way from the root down to the farthest leaf.
For example, a tree with only a root has depth 1, an empty tree has depth 0.

## 2. Approach

I thought about it like this: the depth of a tree = 1 (the root) + the depth of the deeper subtree.

1. If the node is `None` -> return 0.
2. Find the depth of the left subtree (recursive call).
3. Find the depth of the right subtree (recursive call).
4. Return `1 + max(left, right)`.

### Tracing

Example: `root = [3, 9, 20, null, null, 15, 7]`

```
      3
     / \
    9   20
       /  \
      15   7
```

The calls go down first and then the answers come back up:

| Call | left | right | returns |
|------|------|-------|---------|
| maxDepth(9) | 0 (None) | 0 (None) | 1 + max(0, 0) = 1 |
| maxDepth(15) | 0 | 0 | 1 |
| maxDepth(7) | 0 | 0 | 1 |
| maxDepth(20) | 1 (from 15) | 1 (from 7) | 1 + max(1, 1) = 2 |
| maxDepth(3) | 1 (from 9) | 2 (from 20) | 1 + max(1, 2) = **3** |

Answer: 3 - correct.

### Challenges / what did not work

- At first I wrote `if root is None: return 1`, because I thought "every node counts as 1".
  But then a single node gave depth 2 (1 + max(1, 1)), which is wrong. The empty tree must be 0,
  and the `+1` is added only for real nodes.
- I also thought about writing a counter variable that goes up when I go down and goes down when I go back,
  and saving the maximum. It works too, but it was more confusing to keep track of the counter,
  so the simple "1 + max" version is better for me.

### Testing

LeetCode examples, an empty tree, one node, and a "line" tree `[1, 2, null, 3, null, 4]` (depth 4).

## 3. Time and Space Complexity

**Time Complexity: O(n)**.
The function is called one time for every node (and also for the `None` children, but there are only n + 1 of them).
Each call does only constant work: two calls and one `max`. So total work is proportional to n.

**Space Complexity: O(h)**, h = height of the tree.
This is the recursion stack - at the same moment there are at most h calls waiting.
Balanced tree: O(log n). Worst case (tree is a line): O(n).

## 4. Reflection / Improvement

- Time can't be better than O(n): to be sure which path is the longest we have to look at every node.
- Another way is **BFS** (level by level with a queue): count how many levels there are. It is also O(n) time.
  Its space is O(width of the tree) instead of O(height), so it is better for very deep thin trees
  and does not have the risk of recursion limit in Python. For normal LeetCode trees my recursive version is fine.
