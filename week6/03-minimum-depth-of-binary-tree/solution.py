# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        def derevo(node, count):
            if node is None:
                return float('inf')

            if node.left is None and node.right is None:
                return count

            left_derevo = derevo(node.left, count + 1)
            right_derevo = derevo(node.right, count + 1)

            return min(left_derevo, right_derevo)

        return derevo(root, 1)
