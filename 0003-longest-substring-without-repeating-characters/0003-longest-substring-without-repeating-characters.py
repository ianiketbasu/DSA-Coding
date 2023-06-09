class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len , start = 0 , -1
        freq = [-1]*256
        for i in range(0,len(s)) :
            if freq[ord(s[i])] > start :
                start = freq[ord(s[i])]
            freq[ord(s[i])] = i
            max_len = max(max_len , i - start)
        
        return max_len