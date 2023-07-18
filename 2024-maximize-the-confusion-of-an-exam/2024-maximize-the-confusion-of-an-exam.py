class Solution(object):
    def maxConsecutiveAnswers(self, s, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        maxf = res = 0
        count = collections.Counter()
        for i in range(len(s)):
            count[s[i]] += 1
            maxf = max(maxf, count[s[i]])
            if res - maxf < k:
                res += 1
            else:
                count[s[i - res]] -= 1
        return res