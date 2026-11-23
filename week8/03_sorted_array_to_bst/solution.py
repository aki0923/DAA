class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


def print_tree(root):
    result = []
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        if node == None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while len(result) > 0 and result[-1] == None:
        result.pop()
    print(result)


def inorder(root, arr):
    if root == None:
        return
    inorder(root.left, arr)
    arr.append(root.val)
    inorder(root.right, arr)


def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root):
    if root == None:
        return True
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


s = Solution()
tests = [[-10, -3, 0, 5, 9], [1, 3], [1, 2, 3, 4, 5, 6, 7], [5]]

for nums in tests:
    root = s.sortedArrayToBST(nums)
    print("input:", nums)
    print_tree(root)
    arr = []
    inorder(root, arr)
    print("inorder same as input:", arr == nums)
    print("balanced:", is_balanced(root))
    print()
