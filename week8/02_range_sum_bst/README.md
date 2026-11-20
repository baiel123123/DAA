# Range Sum of BST

## 1. Problem
Given the root of a Binary Search Tree and two integers `low` and `high`, calculate the sum of all node values in the tree that fall within the inclusive range `[low, high]`.

## 2. Approach
My solution uses post-order recursion (`derevo(node)`) with BST pruning:
- If `node is None`, return `0`.
- Only explore `node.left` when `node.val > low`, because if `node.val <= low`, no node in the left subtree can be greater than `low`.
- Only explore `node.right` when `node.val < high`, because if `node.val >= high`, no node in the right subtree can be less than `high`.
- If `low <= node.val <= high`, include `node.val + left + right`; otherwise return `left + right`.

### Written Trace
Example: tree `[10, 5, 15, 3, 7, None, 18]`, `low = 7`, `high = 15`:
- **Node `10`:** `10 > 7` -> check left (`5`); `10 < 15` -> check right (`15`). `10` is in `[7, 15]`.
- **Node `5`:** `5 > 7` is false (skip left subtree); `5 < 15` -> check right (`7`). `5` is not in `[7, 15]`.
- **Node `7`:** `7 > 7` false, `7 < 15` true (right is `None` -> `0`). `7` is in `[7, 15]` -> returns `7`.
- **Back to `5`:** returns `0 + 7 = 7`.
- **Node `15`:** `15 > 7` -> check left (`None` -> `0`); `15 < 15` false (skip right subtree). `15` is in `[7, 15]` -> returns `15`.
- **Back to `10`:** `10 + 7 + 15 = 32`.

### Challenges & Tested / Considered Approaches
- **Traversing every node without bounds:** Simpler to write initially, but visits subtrees that cannot possibly contain values in `[low, high]`.
- **Strict vs. inclusive bounds on pruning:** Using `node.val > low` and `node.val < high` for pruning while `low <= node.val <= high` for inclusion avoids missing boundary values or recursing into dead branches.

## 3. Complexity
- **Time Complexity:** `O(n)` in the worst case (e.g., when all nodes fall inside `[low, high]`), where `n` is the number of nodes in the tree.
  - **Why:** Each visited node is processed once in `O(1)` time, and branches outside `[low, high]` are pruned rather than traversed.
- **Space Complexity:** `O(h)` for the recursion call stack (`O(log n)` for a balanced BST, `O(n)` in the worst case).

## 4. Reflection / Improvement
- **Is there a more efficient approach?** Worst-case asymptotic time is still `O(n)`, though an iterative stack/queue approach avoids recursion overhead and can stop early on pruned branches.
- **What would you need to change?** Replace the recursive helper with an explicit stack (`list`) and push only valid children (`node.val > low` and `node.val < high`).
- **What complexity could the improved solution achieve?** `O(n)` time and `O(h)` auxiliary space without recursion stack frames.