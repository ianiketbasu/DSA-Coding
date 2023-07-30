class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}
        def check(i, j):
            if (i, j) not in memo:
                if i > j: return 0
                
                res = check(i, j-1) + 1
                for k in range(i, j):
                    if s[k] == s[j]:
                        res = min(res, check(i, k-1) + check(k, j-1))
                memo[(i, j)] = res
                
            return memo[(i, j)]
        
        s = re.sub(r'(.)\1*', r'\1', s)
        return check(0, len(s) - 1)