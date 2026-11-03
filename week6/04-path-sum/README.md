# Path Sum

## 1. Problem

I need to check if the tree has a path from the root to a leaf where the sum of all node values equals `targetSum`.

## 2. Approach

I use recursion. At each node, I subtract its value from the target sum.

If the node is `None`, I return `False`. If it is a leaf, I check whether the remaining target is equal to its value. Otherwise, I continue searching in the left or right subtree.

I use `or` because only one valid path is needed.

### Example / Tracing

For this path:

```text
    5
   /
  4
 /
11
```

If the target is `20`, I subtract the values one by one:

- `20 - 5 = 15`
- `15 - 4 = 11`
- `11 - 11 = 0`

The leaf matches the remaining sum, so the result is `True`.

## 3. Time Complexity

**Time Complexity: O(n)**

In the worst case, I may need to visit every node.

## 4. Space Complexity

**Space Complexity: O(h)**

The recursive call stack depends on the height of the tree. In the worst case, it can be O(n).

## 5. Reflection / Improvement

The recursive solution is already O(n) in the worst case. I could implement the same search iteratively using a stack.
