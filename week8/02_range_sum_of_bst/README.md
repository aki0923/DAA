# 938. Range Sum of BST

## 1. Problem

We get the root of a binary search tree and two numbers `low` and `high`. We need to add up the values of all nodes that are between `low` and `high` (including `low` and `high` themselves) and return this sum.

## 2. Approach

I did a simple solution: visit every node of the tree with recursion (DFS) and if the value is in the range, add it to the sum.

Steps for each node:
1. If node is `None` -> return 0.
2. If `low <= node.val <= high` -> add `node.val` to total.
3. Add the sum from the left subtree.
4. Add the sum from the right subtree.
5. Return total.

### Tracing

Tree: `[10,5,15,3,7,null,18]`, low = 7, high = 15
```
          10
         /  \
        5    15
       / \     \
      3   7     18
```

| Call | Node | In range [7,15]? | Added | Returns |
|------|------|------------------|-------|---------|
| 1 | 10 | yes | 10 | waits for children |
| 2 | 5 | no | 0 | waits for children |
| 3 | 3 | no | 0 | 0 (children are None) |
| 4 | 7 | yes | 7 | 7 |
| - | back to 5 | | | 0 + 0 + 7 = 7 |
| 5 | 15 | yes | 15 | waits for children |
| 6 | 18 | no | 0 | 0 |
| - | back to 15 | | | 15 + 0 + 0 = 15 |
| - | back to 10 | | | 10 + 7 + 15 = **32** |

Answer = 32. Correct.

Second example: `[10,5,15,3,7,13,18,1,null,6]`, low = 6, high = 10.
Nodes in range: 10, 7, 6 -> 10 + 7 + 6 = **23**. My program also gives 23.

### Challenges

- First I tried to make it faster: if `node.val < low` I returned 0 right away. This was wrong! For example node 5 is less than 7, but its right child 7 is in the range. So I lost 7 and got 25 instead of 32. Then I understood that if node is too small I can skip only the **left** side, not everything. Because it was confusing I decided to just check all nodes, it is always correct.
- Another idea was to do inorder traversal, save all values into a list and then sum the ones in range. It works too but uses an extra list, so I did the sum directly in recursion.
- I mixed up `<` and `<=` at first and test 1 gave 17 (without 15), because the range includes the borders.

### Testing

Tested both examples from LeetCode (32 and 23) and one tree with one node where nothing is in range (answer 0).

## 3. Time Complexity

**Time Complexity: O(n)**, n = number of nodes.

My function is called one time for every node (and for the `None` children, but there are only n + 1 of them). In each call I do only a comparison and addition, which is O(1). So n * O(1) = O(n).

**Space Complexity: O(h)**, h = height of tree.

I don't use any arrays, only recursion. The call stack can have at most h calls at the same time (from root to the deepest leaf). For balanced tree O(log n), for a tree like a linked list O(n).

## 4. Reflection / Improvement

- **Is there a more efficient approach?** Yes, my solution doesn't use the BST property, it works like for any normal tree.
- **What would you need to change?** Skip subtrees that can't have values in range:
  - if `node.val < low` -> everything in the left subtree is also smaller, go only right
  - if `node.val > high` -> everything in the right subtree is also bigger, go only left
  - else -> add value and go both sides
- **What complexity could the improved solution achieve?** Worst case is still **O(n)** (if all nodes are in the range we have to visit all of them anyway). But usually it is much faster, around O(h + k) where k is the number of nodes in the range, because big parts of the tree are skipped. Space stays O(h).
