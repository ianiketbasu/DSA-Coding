class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(2*n) + str(3*n)
        my_set = set(s)
        return len(my_set) == 9 and '0' not in my_set and len(s) == 9
        