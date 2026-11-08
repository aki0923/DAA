# LeetCode 111. Minimum Depth of Binary Tree
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # leaf -> depth is 1
        if root.left is None and root.right is None:
            return 1
        # only one child exists -> we must go to that child,
        # because the empty side is NOT a leaf
        if root.left is None:
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)
        # both children exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    # BFS version: stops at the first leaf it finds
    def minDepthBFS(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([3, 9, 20, None, None, 15, 7], 2),
        ([2, None, 3, None, 4, None, 5, None, 6], 5),
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
    ]
    for values, expected in tests:
        root = build_tree(values)
        assert s.minDepth(root) == expected, values
        assert s.minDepthBFS(root) == expected, values
    print("all tests passed")
