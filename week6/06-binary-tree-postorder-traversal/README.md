# Binary Tree Postorder Traversal

## 1. Problem

I need to return all values of a binary tree using postorder traversal. The order is left subtree, right subtree, and root.

## 2. Approach

I use recursion and one list called `lst`.

If the current node is `None`, I stop the call. Otherwise, I first visit the left child, then the right child, and only after that add the current node value.

### Example / Tracing

For this tree:

```text
    1
   / \\
  2   3
```

First I visit `2`, then `3`. After both children are processed, I add the root `1`.

Result: `[2, 3, 1]`.

## 3. Time Complexity

**Time Complexity: O(n)**

Every node is visited exactly once.

## 4. Space Complexity

**Space Complexity: O(n)**

The result list stores all node values. The recursive call stack uses O(h) additional space, where `h` is the tree height.

## 5. Reflection / Improvement

I could implement this traversal iteratively with a stack. The time complexity would remain O(n), but I would avoid recursive calls.
