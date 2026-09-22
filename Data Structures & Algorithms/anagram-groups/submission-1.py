class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in groups.keys():
                groups[sorted_str] = list()
            groups[sorted_str].append(s)
        group_anagram = [l for l in groups.values()]
        return group_anagram