# Binary Search

## Problem

Given a sorted array and a target number, find the index of the target. If it is not found, return -1.

## Approach

I used binary search. I have `left` and `right` variables that show the current search range.

I find the middle element and compare it with the target.

If the target is bigger, I move `left` to the right. If the target is smaller, I move `right` to the left.

I repeat this until I find the target or there are no elements left.

## Time Complexity

O(log n)

The search range becomes about two times smaller after each iteration.

## Space Complexity

O(1)

I only use a few variables and do not create any additional data structures.

## Improvement

This solution is already using binary search, so it has good time complexity. A simple loop through all elements would be O(n), which is slower.
