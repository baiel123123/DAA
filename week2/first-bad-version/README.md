# First Bad Version

## Problem

There are `n` versions. After the first bad version, all following versions are also bad. We need to find the first bad version.

## Approach

I used binary search.

I have `left` and `right` variables for the current range of versions. I check the middle version using `isBadVersion()`.

If the middle version is good, I search on the right side. If it is bad, I search on the left side.

I repeat this until I find the first bad version.

## Time Complexity

O(log n)

After each iteration, about half of the versions can be removed from the search.

## Space Complexity

O(1)

I only use `left`, `right` and `mid`, so the additional memory does not depend on the number of versions.

## Improvement

The solution already uses binary search. However, I could reduce the number of calls to `isBadVersion()` by avoiding repeated checks of the same version.
