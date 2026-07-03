# LeetCode 2016 - Maximum Difference Between Increasing Elements

## Problem

Given a 0-indexed integer array `nums` of size `n`, find the maximum difference between `nums[i]` and `nums[j]` such that:

- `0 <= i < j < n`
- `nums[i] < nums[j]`

Return the maximum difference. If no such pair exists, return `-1`.

---

## Approach

- Keep track of the minimum element seen so far.
- For each element:
  - If it is greater than the minimum, calculate the difference.
  - Update the maximum difference.
  - Otherwise, update the minimum element.
- Return the maximum difference found.

---

## Python Solution

```python
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min1 = nums[0]
        max1 = -1

        for i in range(1, len(nums)):
            if nums[i] > min1:
                max1 = max(max1, nums[i] - min1)
            else:
                min1 = nums[i]

        return max1
```

## Example

### Input

```python
nums = [7, 1, 5, 4]
```

### Output

```python
4
```

### Explanation

- Minimum element encountered: `1`
- Maximum valid difference: `5 - 1 = 4`

---

## Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Key Insight

For every position `j`, the best possible `i` is the smallest element that appeared before `j`. Therefore, we only need to keep track of the minimum value seen so far while traversing the array once.
