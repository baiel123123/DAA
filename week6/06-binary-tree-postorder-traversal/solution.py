# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        lst = []

        def traversal(node):
            if node is None:
                return

            traversal(node.left)
            traversal(node.right)
            lst.append(node.val)

        traversal(root)
        return lst
