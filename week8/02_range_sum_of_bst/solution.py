class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root, low, high):
        if root == None:
            return 0
        total = 0
        if root.val >= low and root.val <= high:
            total = total + root.val
        total = total + self.rangeSumBST(root.left, low, high)
        total = total + self.rangeSumBST(root.right, low, high)
        return total


s = Solution()

# tree 1: [10,5,15,3,7,null,18]
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

print("test 1:", s.rangeSumBST(root, 7, 15), "expected 32")

# tree 2: [10,5,15,3,7,13,18,1,null,6]
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.right = TreeNode(15)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(13)
root2.right.right = TreeNode(18)
root2.left.left.left = TreeNode(1)
root2.left.right.left = TreeNode(6)

print("test 2:", s.rangeSumBST(root2, 6, 10), "expected 23")

# one node
print("test 3:", s.rangeSumBST(TreeNode(5), 1, 4), "expected 0")
