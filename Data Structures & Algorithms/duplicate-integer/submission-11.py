class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        none_duplicate = set()
        for i in nums:
            if i in none_duplicate:
                return True
            none_duplicate.add(i)
        return False