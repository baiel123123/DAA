from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def array(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            node.left = array(left, mid - 1)
            node.right = array(mid + 1, right)

            return node

        return array(0, len(nums) - 1)


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []
    result: list[int | None] = []
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr is None:
            result.append(None)
        else:
            result.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    solver = Solution()
    t1 = solver.sortedArrayToBST([-10, -3, 0, 5, 9])
    print("Test 1:", tree_to_list(t1))  # e.g., [0, -10, 5, None, -3, None, 9]

    t2 = solver.sortedArrayToBST([1, 3])
    print("Test 2:", tree_to_list(t2))  # e.g., [1, None, 3] or [3, 1]