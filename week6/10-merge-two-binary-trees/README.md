# Merge Two Binary Trees

## 1. Problem

I need to merge two binary trees. If both trees have a node in the same position, I add their values. If only one tree has a node in that position, I keep that node.

## 2. Approach

I use recursion.

If the first node is `None`, I return the second node. If the second node is `None`, I return the first node.

If both nodes exist, I add the second node value to the first one. Then I recursively merge their left children and their right children. I return the first root as the merged tree.

### Example / Tracing

First tree:

```text
    1
   /
  3
```

Second tree:

```text
    2
     \\
      4
```

The roots are both present, so `1 + 2 = 3`. The left child `3` from the first tree stays, and the right child `4` from the second tree is added.

Merged tree:

```text
    3
   / \\
  3   4
```

## 3. Time Complexity

**Time Complexity: O(min(n, m))**

I recursively process positions where both trees have nodes. The number of such positions cannot be greater than the number of nodes in the smaller tree.

## 4. Space Complexity

**Space Complexity: O(min(h1, h2))**

The recursive calls continue while both corresponding nodes exist. The call stack depends on the overlapping height of the two trees.

## 5. Reflection / Improvement

This solution modifies the first tree instead of creating a completely new tree. I could create new nodes to preserve both original trees, but that would require additional memory.
