class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # counter1 = counter2 = Counter()
        return Counter(ch for ch in s)==Counter(ch for ch in t)
        