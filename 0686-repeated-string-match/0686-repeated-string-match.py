class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # times = -(-len(B) // len(A))  # Equal to ceil(len(B) / len(A))
        # print(times)
        # for i in range(2):
        #     print((A * (times + i)))
        #     if B in (A * (times + i)):
        #         return times + i
        # return -1
    
    
    
        my_str = a
        count = 1
        n = len(b)//len(a)
        
        for i in range(n+2) :
            if b in (my_str*(i+1)) :
                return count
            else :
                count += 1
                # my_str += a
        
        return -1