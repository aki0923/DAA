# LeetCode 617. Merge Two Binary Trees
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


def tree_to_list(root):
    # turns tree back into leetcode list so I can check the answer
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if one of them is missing, just take the other one (it can be None too)
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        # both exist -> new node with the sum
        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], [3, 4, 5, 5, 4, None, 7]),
        ([1], [1, 2], [2, 2]),
        ([], [], []),
        ([], [1, 2], [1, 2]),
        ([5, 1], [], [5, 1]),
    ]
    for a, b, expected in tests:
        result = s.mergeTrees(build_tree(a), build_tree(b))
        assert tree_to_list(result) == expected, (a, b)
    print("all tests passed")
