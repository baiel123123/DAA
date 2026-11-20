# Convert Sorted Array to Binary Search Tree

## 1. Problem
Given an integer array `nums` sorted in strictly increasing order, construct a height-balanced Binary Search Tree (where the depths of the two subtrees of every node differ by at most `1`).

## 2. Approach
My solution uses divide-and-conquer recursion (`array(left, right)`) over index boundaries:
1. If `left > right`, the subarray is empty, so return `None`.
2. Pick `mid = (left + right) // 2` as the root of the current range so roughly half of the remaining elements go to the left subtree and half to the right.
3. Create `node = TreeNode(nums[mid])`, recursively build `node.left` from `[left, mid - 1]` and `node.right` from `[mid + 1, right]`, and return `node`.

### Written Trace
Example: `nums = [-10, -3, 0, 5, 9]`, initial call `array(0, 4)`:
- `mid = (0 + 4) // 2 = 2` -> root `TreeNode(0)`.
- Left child `array(0, 1)`: `mid = 0` -> `TreeNode(-10)`; left `array(0, -1)` is `None`, right `array(1, 1)` -> `TreeNode(-3)`.
- Right child `array(3, 4)`: `mid = 3` -> `TreeNode(5)`; left `array(3, 2)` is `None`, right `array(4, 4)` -> `TreeNode(9)`.
- Resulting tree has root `0` and is height-balanced.

### Challenges & Tested / Considered Approaches
- **Picking the first or last element as root:** Leads to a skewed linked-list-like tree instead of a height-balanced BST.
- **Slicing arrays (`nums[:mid]`, `nums[mid+1:]`):** Works logically, but creates extra sub-lists and copies elements at each step; passing `left` and `right` indices avoids unnecessary slice allocations.

## 3. Complexity
- **Time Complexity:** `O(n)`, where `n` is the length of `nums`.
  - **Why:** Each element in `nums` is chosen as `nums[mid]` once to create a `TreeNode`, and index arithmetic takes `O(1)` time per call.
- **Space Complexity:** `O(log n)` for the recursion call stack (excluding the `O(n)` output tree itself), since the resulting tree is height-balanced.

## 4. Reflection / Improvement
- **Is there a more efficient approach?** Asymptotic `O(n)` time is already optimal because every element must be placed into a node, though iterative tree construction or using `(left + right) // 2` vs `left + (right - left) // 2` are minor implementation details.
- **What would you need to change?** If implementing iteratively, maintain an explicit stack of `(left, right, parent, is_left)` tuples instead of recursive calls.
- **What complexity could the improved solution achieve?** `O(n)` time and `O(log n)` auxiliary stack space (plus `O(n)` for the output tree).