class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for k,i in enumerate(nums):
            if i in nums[k+1:]:
                return True
        return False