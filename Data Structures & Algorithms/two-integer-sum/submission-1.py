class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, e1 in enumerate(nums):
            for i2 in range(i+1, len(nums)):
                if (e1 + nums[i2]) == target:
                    return [i, i2]
        return []