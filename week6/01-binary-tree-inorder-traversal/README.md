# Binary Tree Inorder Traversal

## 1. Problem

I need to return the values of a binary tree using inorder traversal. The order is left subtree, root, and right subtree.

## 2. Approach

I use recursion and one list called `lst`.

If the current node is `None`, I stop this recursive call. Otherwise, I first visit the left child, append the current node value, and then visit the right child.

### Example / Tracing

For this tree:

```text
    1
   / \\
  2   3
```

The traversal goes to the left child `2`, adds `2`, then adds the root `1`, and finally adds `3`.

Result: `[2,  1, 3]`.

## 3. Time Complexity

**Time Complexity: O(n)**

I visit every node exactly once, where `n` is the number of nodes.

## 4. Space Complexity

**Space Complexity: O(n)**

The result list stores all `n` values. The recursive calls also use stack space depending on the tree height.

## 5. Reflection / Improvement

The recursive solution is simple and easy to understand. I could also use an iterative solution with a stack to avoid recursion.
