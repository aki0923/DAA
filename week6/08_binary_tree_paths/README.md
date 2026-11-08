# 257. Binary Tree Paths

Link: https://leetcode.com/problems/binary-tree-paths/

Code: [solution.py](solution.py)

## 1. Problem

Return all paths from the root to every leaf, as strings like `"1->2->5"`.

## 2. Approach

DFS where I carry the path so far as a string:

1. If node is `None` -> return.
2. Add the current value to the path. If the path is empty, the path is just the value,
   otherwise `path + "->" + value`.
3. If the node is a leaf -> the path is complete, add it to the result.
4. Otherwise go left and right with the new path.

Strings in Python can't be changed, so each call gets its own copy of the path and I don't need to "undo" anything
when I go back up.

### Tracing

Example: `root = [1, 2, 3, null, 5]`

```
    1
   / \
  2   3
   \
    5
```

| Call | path inside the call | leaf? | result |
|------|---------------------|-------|--------|
| dfs(1, "") | "1" | no | [] |
| dfs(2, "1") | "1->2" | no | [] |
| dfs(None, "1->2") (left of 2) | - | - | return |
| dfs(5, "1->2") | "1->2->5" | yes | ["1->2->5"] |
| dfs(3, "1") | "1->3" | yes | ["1->2->5", "1->3"] |

Notice that when I go to node 3, the path is `"1"` again, not `"1->2->5"`, because each call has its own string.

Answer: `["1->2->5", "1->3"]`.

### Challenges / what did not work

- At first I used one shared **list** for the path and did `path.append(node.val)`. I forgot to remove the value
  when going back, so the second path became `"1->2->5->3"`. With a list you have to do `path.pop()` after the
  recursive calls (backtracking). I switched to strings because then the problem just doesn't happen.
- My next version was `path + str(node.val) + "->"` and then I got paths like `"1->2->5->"` with an extra arrow
  at the end. So I changed it to put the arrow **before** the value, and the first value has no arrow.
- I also tried to add the path when `node is None` instead of at the leaf. Then for node 2 (which has only a right
  child) I got the path `"1->2"` too, which is wrong because 2 is not a leaf. Same mistake as in Path Sum.

### Testing

LeetCode examples, one node, `[1, 2]`, negative numbers (to check that `-` signs look ok), empty tree.

## 3. Time and Space Complexity

**Time Complexity: O(n * h)**, in the worst case O(n^2).
We visit every node one time, but in every node we build a new string `path + "->" + value`,
and making a new string copies the whole old string. The path length is up to h (height).
So it is n nodes times up to h characters copied.
For a balanced tree this is about O(n log n). For a tree like a line it is O(n^2).
(Also the answer itself can be big: number of leaves times path length.)

**Space Complexity: O(h^2)** for the recursion: h calls on the stack, and each one holds a string of up to h values.
Plus the output list. For a balanced tree that is small; in the worst case it is O(n^2).

## 4. Reflection / Improvement

- Better: use one list `path` with `append` / `pop` (backtracking) and only do `"->".join(path)` when I reach a leaf.
  Then going down costs O(1) per node and the string is built only for complete paths.
- The time is then O(n + total length of all output strings). The output size itself can't be avoided,
  so this is the best possible, but it removes the extra copying on nodes that are not leaves.
- Extra space becomes O(h) for the path list and the stack.
