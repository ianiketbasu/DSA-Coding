class Solution(object):
    def maxValue(self, A, K):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        A.sort(key=lambda sev: sev[1])
        dp, dp2 = [[0, 0]], [[0, 0]]
        for k in xrange(K):
            for s, e, v in A:
                i = bisect.bisect(dp, [s]) - 1
                if dp[i][1] + v > dp2[-1][1]:
                    dp2.append([e, dp[i][1] + v])
            dp, dp2 = dp2, [[0, 0]]
        return dp[-1][-1]