class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        my_str = a
        count = 1
        n = len(b)//len(a)
        
        for i in range(n+2) :
            if b in my_str :
                return count
            else :
                count += 1
                my_str += a
        
        return -1
        