# Sum of Left Leaves

## 1. Problem

I need to calculate the sum of all left leaves in a binary tree. A left leaf is a node that is both a left child and has no children.

## 2. Approach

I use recursion and pass an additional argument `is_left` to know if the current node is a left child.

If the node is `None`, I return 0. If it is a leaf, I return its value only when `is_left` is `True`. Otherwise, I calculate the sums from the left and right subtrees and add them.

### Example / Tracing

```text
      3
     / \\
    9   20
       /  \\
      15   7
```

The left leaves are `9` and `15`. The node `7` is a right leaf, so I do not include it.

The sum is `9 + 15 = 24`.

## 3. Time Complexity

**Time Complexity: O(n)**

I visit every node once to check whether it is a left leaf.

## 4. Space Complexity

**Space Complexity: O(h)**

The recursive call stack depends on the height of the tree. In the worst case, it can be O(n).

## 5. Reflection / Improvement

The recursive solution is already O(n). I could use an iterative stack and store whether each node is a left child.
