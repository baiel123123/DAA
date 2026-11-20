from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        def tree(node: TreeNode | None) -> TreeNode | None:
            if node is None:
                return None

            if node.val == val:
                return node

            if val < node.val:
                return tree(node.left)
            else:
                return tree(node.right)

        return tree(root)


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
    root1 = build_tree([4, 2, 7, 1, 3])
    found1 = solver.searchBST(root1, 2)
    print("Test 1 (val=2):", tree_to_list(found1)) 
    root2 = build_tree([4, 2, 7, 1, 3])
    found2 = solver.searchBST(root2, 5)
    print("Test 2 (val=5):", tree_to_list(found2)) 