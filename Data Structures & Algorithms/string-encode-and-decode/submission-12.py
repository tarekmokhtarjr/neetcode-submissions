class Solution:

    def encode(self, strs: List[str]) -> str:
        return "-sep-".join(strs) if len(strs) > 0 or len(strs) > 99 else "None"

    def decode(self, s: str) -> List[str]:
        try:
            s.encode("utf-8")
            return s.split("-sep-") if s != "None" or len(str) > 199 else []
        except:
            return []
