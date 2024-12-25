from typing import List

"""
1. using divide and conquire , split equally 
2. find max in the left and rights
3. find left mid and right mid max (cross max)

4. using kadane's algorithm

"""


# using kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum = float("-inf")
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(current_sum, max_sum)
        return max_sum


Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
