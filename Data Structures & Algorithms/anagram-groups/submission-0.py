class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if sorted(s) == sorted(t):
                return True
            return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = dict()
        for i in range(0, len(strs)):
            x = sorted(strs[i])
            tmp = []
            for e in strs:
                if self.isAnagram(strs[i], e):
                    tmp.append(e)
            grouped_anagrams["".join(x)] = tmp
        grouped_anagrams_list = [v for v in grouped_anagrams.values()]
        return grouped_anagrams_list