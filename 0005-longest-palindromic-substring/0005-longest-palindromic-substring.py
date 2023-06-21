class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1 : return s
        start , end ,max_len= 0 , 0 , 1
        
        # For odd length
        for i in range(0,n-1) :
            l , r = i , i
            while(l>-1 and r < n) :
                if s[l] == s[r] :
                    l-=1
                    r+=1
                else :
                    break
            
            length = r-l-1
            if length > max_len :
                max_len = length
                start , end = l + 1 , r - 1
        
        # For even length
        for i in range(0,n-1) :
            l , r = i , i+1
            while(l>-1 and r < n) :
                if s[l] == s[r] :
                    l-=1
                    r+=1
                else :
                    break
            
            length = r-l-1
            if length > max_len :
                max_len = length
                start , end = l + 1 , r - 1
        
        return s[start:end+1]
            