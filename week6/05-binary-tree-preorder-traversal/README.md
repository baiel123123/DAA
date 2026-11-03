# Binary Tree Preorder Traversal

## 1. Problem

I need to return all values of a binary tree using preorder traversal. The order is root, left subtree, and right subtree.

## 2. Approach

I use recursion and a list called `lst`.

If the current node is `None`, I stop the call. Otherwise, I first add the current node value to the list, then visit the left child, and after that visit the right child.

### Example / Tracing

For this tree:

```text
    1
   / \\
  2   3
```

First I add the root `1`. Then I visit and add `2`. After returning, I visit and add `3`.

Result: `[1, 2, 3]`.

## 3. Time Complexity

**Time Complexity: O(n)**

Every node is visited and added to the list exactly once.

## 4. Space Complexity

**Space Complexity: O(n)**

The result list stores all node values. The recursive call stack uses O(h) additional space, where `h` is the tree height.

## 5. Reflection / Improvement

I could use an iterative solution with a stack. The time complexity would still be O(n), but it would not use recursive calls.
