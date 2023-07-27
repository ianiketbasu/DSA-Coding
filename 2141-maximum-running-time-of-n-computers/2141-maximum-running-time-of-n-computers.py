class Solution(object):
    def maxRunTime(self, n, A):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        A.sort()
        su = sum(A)
        while A[-1] > su / n:
            n -= 1
            su -= A.pop()
        return su / n