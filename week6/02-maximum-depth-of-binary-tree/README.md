# Maximum Depth of Binary Tree

## 1. Problem

I need to find the maximum depth of a binary tree. The depth is the number of nodes on the longest path from the root to a leaf.

## 2. Approach

I use recursion and pass the current depth as an argument.

For every node, I increase the depth by one and calculate the depth of the left and right subtrees. When the node is `None`, I return the current depth. At the end, I return the bigger result.

### Example / Tracing

For this tree:

```text
    1
   / \\
  2   3
 /
4
```

The left path is `1 -> 2 -> 4`, so its depth is 3. The right path is `1 -> 3`, so its depth is 2.

The answer is `3`.

## 3. Time Complexity

**Time Complexity: O(n)**

Every node is visited once to calculate the depths of both subtrees.

## 4. Space Complexity

**Space Complexity: O(h)**

The recursive calls are stored on the call stack. `h` is the height of the tree. In the worst case, it can be O(n).

## 5. Reflection / Improvement

The solution already visits every node only once, so its time complexity is optimal. I could use an iterative BFS approach with a queue instead of recursion.
