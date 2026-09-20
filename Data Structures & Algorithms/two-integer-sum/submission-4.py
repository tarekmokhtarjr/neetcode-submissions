class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for k,e in enumerate(nums):
            if (target - e) in nums[k+1:]:
                nums[k] = ""
                return [k, nums.index(target-e)]
        return [] 