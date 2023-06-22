class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(ch for ch in s)==Counter(ch for ch in t)
        return Counter(s)==Counter(t)
        
        