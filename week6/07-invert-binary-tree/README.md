# Invert Binary Tree

## 1. Problem

I need to invert a binary tree. This means swapping the left and right child of every node.

## 2. Approach

I use recursion. If the current node is `None`, I return `None`.

For each node, I swap its left and right children. Then I recursively invert both children. At the end, I return the root of the modified tree.

### Example / Tracing

Before:

```text
    1
   / \\
  2   3
```

I swap the children of `1`, so `3` becomes the left child and `2` becomes the right child.

After:

```text
    1
   / \\
  3   2
```

I do the same operation for every other node.

## 3. Time Complexity

**Time Complexity: O(n)**

I visit every node once and swap its children.

## 4. Space Complexity

**Space Complexity: O(h)**

The recursive call stack depends on the height of the tree. In the worst case, it can be O(n).

## 5. Reflection / Improvement

The solution already visits every node once. I could use an iterative approach with a queue or stack instead of recursion.
