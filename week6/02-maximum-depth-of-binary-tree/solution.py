# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        def dep(node, depth):
            if not node:
                return depth

            left_depth = dep(node.left, depth + 1)
            right_depth = dep(node.right, depth + 1)

            return max(left_depth, right_depth)

        return dep(root, 0)
