# LeetCode 145. Binary Tree Postorder Traversal
from collections import deque
from typing import List, Optional


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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)           # 1. left subtree
            dfs(node.right)          # 2. right subtree
            result.append(node.val)  # 3. current node last

        dfs(root)
        return result

    # stack version: do "node, right, left" and then reverse the list
    # node-right-left reversed = left-right-node = postorder
    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        result.reverse()
        return result


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([1, None, 2, 3], [3, 2, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 6, 7, 5, 2, 9, 8, 3, 1]),
    ]
    for values, expected in tests:
        root = build_tree(values)
        assert s.postorderTraversal(root) == expected, values
        assert s.postorderTraversalIterative(root) == expected, values
    print("all tests passed")
