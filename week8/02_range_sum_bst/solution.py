from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        def derevo(node: TreeNode | None) -> int:
            if node is None:
                return 0

            left = 0
            right = 0

            if node.val > low:
                left = derevo(node.left)

            if node.val < high:
                right = derevo(node.right)

            if low <= node.val <= high:
                return node.val + left + right
            else:
                return left + right

        return derevo(root)


def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        curr = queue.popleft()
        if i < len(values) and values[i] is not None:
            curr.left = TreeNode(values[i])
            queue.append(curr.left)
        i += 1
        if i < len(values) and values[i] is not None:
            curr.right = TreeNode(values[i])
            queue.append(curr.right)
        i += 1
    return root


if __name__ == "__main__":
    solver = Solution()
    root1 = build_tree([10, 5, 15, 3, 7, None, 18])
    print("Test 1 (low=7, high=15):", solver.rangeSumBST(root1, 7, 15))  # Expected: 32

    root2 = build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
    print("Test 2 (low=6, high=10):", solver.rangeSumBST(root2, 6, 10))  # Expected: 23