# Binary Tree Paths

## 1. Problem

I need to return all paths from the root to every leaf. Each path must be represented as a string with `->` between node values.

## 2. Approach

I use recursion and pass the current path as an argument.

If the node is `None`, I stop. Otherwise, I add its value to the path. If it is a leaf, I add the completed path to the result list. If it is not a leaf, I add the arrow and continue with the left and right children.

### Example / Tracing

For this tree:

```text
    1
   / \\
  2   3
   \\
    5
```

The first path is `1->2->5`. The second path is `1->3`.

Result: `["1->2->5", "1->3"]`.

## 3. Time Complexity

**Time Complexity: O(n + output)**

I visit every node. I also build and store the path strings. In a very unbalanced tree, the total length of the returned strings can be O(n²).

## 4. Space Complexity

**Space Complexity: O(n²) including the result**

The result can contain path strings whose total length is O(n²) in the worst case. The recursive call stack and current path use additional space depending on the tree height.

## 5. Reflection / Improvement

I could pass a list of node values instead of creating a new string at each step. This can reduce repeated string copying, but the returned strings still need to be created.
