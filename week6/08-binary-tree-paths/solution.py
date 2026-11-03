# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        lst = []

        def derevo(node, path):
            if node is None:
                return

            path += str(node.val)

            if node.left is None and node.right is None:
                lst.append(path)
                return

            path += "->"
            derevo(node.left, path)
            derevo(node.right, path)

        derevo(root, "")
        return lst
