class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        
        for tup in zip(*strs):
            if len(set(tup)) == 1 :
                ans += tup[0]
            else :
                break
        return ans
        