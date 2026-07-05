class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, e in enumerate(nums):
            if e in nums[i+1:]:
                return True
        return False

        