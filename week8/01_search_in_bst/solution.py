class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val):
        if root == None:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


def print_tree(root):
    if root == None:
        print("[]")
        return
    result = []
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        result.append(node.val)
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    print(result)


# tree: [4,2,7,1,3]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

s = Solution()

print("test 1 (val = 2):")
print_tree(s.searchBST(root, 2))

print("test 2 (val = 5):")
print_tree(s.searchBST(root, 5))

print("test 3 (val = 7):")
print_tree(s.searchBST(root, 7))

print("test 4 (empty tree):")
print_tree(s.searchBST(None, 1))
