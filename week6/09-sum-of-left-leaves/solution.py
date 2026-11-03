# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:

        def derevo(node, is_left):
            if node is None:
                return 0

            if node.left is None and node.right is None:
                if is_left:
                    return node.val
                return 0

            left_sum = derevo(node.left, True)
            right_sum = derevo(node.right, False)

            return left_sum + right_sum

        return derevo(root, False)
