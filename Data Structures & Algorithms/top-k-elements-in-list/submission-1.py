class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        grouped = dict()
        for i in range(0, len(nums)):
            tmp = []
            for e in nums:
                if nums[i] == e:
                    tmp.append(e)
            grouped[nums[i]] = len(tmp)
        frequent_list = []
        for key,el in grouped.items():
            frequent_list.append((el,key))
        return [f[1] for f in sorted(frequent_list)[-k:]]