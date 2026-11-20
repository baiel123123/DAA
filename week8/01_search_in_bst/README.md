# Search in a Binary Search Tree

## 1. Problem
Given a Binary Search Tree (BST) and a target integer `val`, find the node whose value equals `val` and return the subtree rooted at that node. If no such node exists in the tree, return `None`.

## 2. Approach
My solution uses top-down recursion (`tree(node)`) taking advantage of the BST ordering property: all values in the left subtree are smaller than `node.val`, and all values in the right subtree are larger.

At each node:
1. If `node is None`, return `None`.
2. If `node.val == val`, return `node`.
3. If `val < node.val`, recurse into `node.left`; otherwise recurse into `node.right`.

### Written Trace
Example: tree with root `4`, left child `2` (children `1`, `3`), right child `7`, searching for `val = 2`:
- **Call 1 (`node = 4`):** `4 != 2`. Since `2 < 4`, call `tree(node.left)` -> `node = 2`.
- **Call 2 (`node = 2`):** `2 == 2`. Return node `2` (subtree `[2, 1, 3]`).

### Challenges & Tested / Considered Approaches
- **Full tree traversal (DFS/BFS without pruning):** Visiting every node works on any binary tree, but ignores BST ordering and wastes work checking branches that cannot contain `val`.
- **Base case handling:** Making sure `None` is explicitly returned both when reaching a leaf's child and when `val` is absent so callers receive `None` cleanly.

## 3. Complexity
- **Time Complexity:** `O(h)`, where `h` is the height of the tree. On average (balanced BST), this is `O(log n)`; in the worst case (skewed tree), `h = n`, giving `O(n)`.
  - **Why:** At each recursive step, we move down one level and discard the other subtree, so we follow at most one root-to-leaf path of length `h`.
- **Space Complexity:** `O(h)` (`O(log n)` average, `O(n)` worst case) due to the recursion call stack.

## 4. Reflection / Improvement
- **Is there a more efficient approach?** Asymptotically the worst/average bound is still `O(h)`, though an iterative `while` loop avoids recursion call stack overhead.
- **What would you need to change?** Replace the inner recursive function `tree` with a `while node is not None:` loop updating `node = node.left` or `node = node.right`.
- **What complexity could the improved solution achieve?** Time remains `O(h)` (`O(log n)` balanced, `O(n)` skewed), while auxiliary space improves to `O(1)`.