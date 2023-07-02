class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        nr = len(requests)
        res = 0

        def test(mask):
            outd = [0] * n
            ind = [0] * n
            for k in xrange(nr):
                if (1 << k) & mask:
                    outd[requests[k][0]] += 1
                    ind[requests[k][1]] += 1
            return sum(outd) if outd == ind else 0

        for i in xrange(1 << nr):
            res = max(res, test(i))
        return res