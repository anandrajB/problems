from typing import Optional , List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index , data  in enumerate(nums):
            found_data = target - data
            if found_data in seen:
                return [seen[found_data] , index]
            seen[data] = index

