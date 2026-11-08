# LeetCode 404. Sum of Left Leaves
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    # builds a tree from a list like on leetcode, None means no node
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node, is_left):
            if node is None:
                return 0
            # it is a leaf and it came from the left side
            if node.left is None and node.right is None:
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False)

        # root is not a left child of anyone
        return dfs(root, False)


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([3, 9, 20, None, None, 15, 7], 24),
        ([1], 0),
        ([1, 2, 3, 4, 5], 4),
        ([], 0),
        ([1, None, 2, 3], 3),
    ]
    for values, expected in tests:
        assert s.sumOfLeftLeaves(build_tree(values)) == expected, values
    print("all tests passed")
