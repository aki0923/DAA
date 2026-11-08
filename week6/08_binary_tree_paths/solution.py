# LeetCode 257. Binary Tree Paths
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node, path):
            if node is None:
                return
            # add current value to the path string
            if path == "":
                path = str(node.val)
            else:
                path = path + "->" + str(node.val)
            # leaf -> the path is finished
            if node.left is None and node.right is None:
                result.append(path)
                return
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return result


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([1, 2, 3, None, 5], ["1->2->5", "1->3"]),
        ([1], ["1"]),
        ([1, 2], ["1->2"]),
        ([-1, 2, -3], ["-1->2", "-1->-3"]),
        ([], []),
    ]
    for values, expected in tests:
        assert s.binaryTreePaths(build_tree(values)) == expected, values
    print("all tests passed")
