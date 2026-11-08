# 111. Minimum Depth of Binary Tree

Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/

Code: [solution.py](solution.py)

## 1. Problem

We need to find the number of nodes on the shortest way from the root to the closest **leaf**.
A leaf is a node that has no children at all. This "leaf" part is the most important thing in this task.

## 2. Approach

Recursion with 4 cases:

1. Node is `None` -> return 0 (only happens when the whole tree is empty).
2. Node is a leaf (no left, no right) -> return 1.
3. Node has only one child -> we can't stop on the empty side, so return `1 + minDepth(that child)`.
4. Node has both children -> return `1 + min(minDepth(left), minDepth(right))`.

### Tracing

Example 1: `root = [3, 9, 20, null, null, 15, 7]`

```
      3
     / \
    9   20
       /  \
      15   7
```

| Call | case | returns |
|------|------|---------|
| minDepth(9) | leaf | 1 |
| minDepth(15) | leaf | 1 |
| minDepth(7) | leaf | 1 |
| minDepth(20) | both children | 1 + min(1, 1) = 2 |
| minDepth(3) | both children | 1 + min(1, 2) = **2** |

Answer: 2 (path 3 -> 9).

Example 2: `root = [2, null, 3, null, 4, null, 5, null, 6]` - the tree is a line going right:

```
2
 \
  3
   \
    4
     \
      5
       \
        6
```

| Call | case | returns |
|------|------|---------|
| minDepth(6) | leaf | 1 |
| minDepth(5) | only right child | 1 + 1 = 2 |
| minDepth(4) | only right child | 1 + 2 = 3 |
| minDepth(3) | only right child | 1 + 3 = 4 |
| minDepth(2) | only right child | 1 + 4 = **5** |

Answer: 5 - correct.

### Challenges / what did not work

- My first idea was to copy my Max Depth solution and just change `max` to `min`:
  `return 1 + min(minDepth(left), minDepth(right))`.
  It worked on example 1, but on example 2 it returned **1** instead of 5.
  Why: for node 2 the left child is `None`, so `minDepth(None) = 0`, and `1 + min(0, ...) = 1`.
  So the code thought there is a leaf on the empty side, but an empty side is not a leaf.
  That is why I added the special cases for "only one child".
- I also tested `[1, 2]` (root with only a left child). Correct answer is 2, and my wrong version also gave 1 there.

### Testing

Both LeetCode examples, empty tree, one node, `[1, 2]`. I also wrote a BFS version and checked that both give the same results.

## 3. Time and Space Complexity

**Time Complexity: O(n)**.
In the worst case the recursion visits every node one time, and each visit is constant work.

**Space Complexity: O(h)** for the recursion stack, where h is the height.
Balanced tree: O(log n), tree like a line: O(n).

## 4. Reflection / Improvement

- The recursive version always goes through the **whole** tree, even if there is a leaf very close to the root.
- A better way is **BFS** (level by level). The first leaf we meet in BFS is for sure the closest one,
  so we can stop right there. I wrote it in the code as `minDepthBFS`.
- Worst case for BFS is still O(n) time, but in many trees (for example, a huge tree where the root has a leaf child)
  it stops very early. Space for BFS is O(width of the level).
