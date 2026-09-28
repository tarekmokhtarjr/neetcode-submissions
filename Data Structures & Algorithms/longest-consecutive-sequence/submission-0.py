class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        groups = dict()
        idx = 1
        unique_list = set(nums)
        sorted_nums = sorted([i for i in unique_list])
        groups.update({idx:set([sorted_nums[0]])})
        for k,n in enumerate(sorted_nums):
            if k+1 == len(sorted_nums):
                break
            if sorted_nums[k]+1 == sorted_nums[k+1]:
                s = groups.get(idx, set())
                s.add(sorted_nums[k+1])
                groups.update({idx: s})
            else:
                idx += 1
                groups.update({idx: set([sorted_nums[k+1]])})
        lengths = [len(l) for l in groups.values()]
        return max(lengths)