class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        for i in xrange(len(A)):
            for j in xrange(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())