# Minimum Depth of Binary Tree

## 1. Problem

I need to find the minimum depth of a binary tree. It is the number of nodes on the shortest path from the root to a leaf.

## 2. Approach

I use recursion and pass the current node count.

If the node is `None`, I return infinity. This is important because an empty child must not be treated as a leaf. If the current node has no children, I return its current count.

Otherwise, I calculate the minimum depth of the left and right subtrees and return the smaller value.

### Example / Tracing

```text
    1
   /
  2
   \\
    3
```

The root has only a left child, so I cannot count the missing right child as a leaf. The path to the real leaf is `1 -> 2 -> 3`.

The answer is `3`.

## 3. Time Complexity

**Time Complexity: O(n)**

In the worst case, I visit every node to find the closest leaf.

## 4. Space Complexity

**Space Complexity: O(h)**

The recursive call stack depends on the height of the tree. In the worst case, it can be O(n).

## 5. Reflection / Improvement

The solution checks all necessary nodes. An iterative BFS approach could be more efficient in practice because it can stop as soon as it finds the first leaf.
