import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if (
            len(nums) >= 2
            and len(nums) <= 1000
        ):
            return [math.prod(nums[:i] + nums[i + 1 :]) for i in range(0, len(nums))]
        return []
        