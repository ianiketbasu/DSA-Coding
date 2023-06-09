#Your task is to complete this function
#Your should return the required output
from collections import Counter

class Solution:
    def maxLen(self, n, arr):
        count , sum_ = 0 , 0
        dict_ = {0:-1}
        
        for i in range(0,n):
            sum_ += arr[i]
            if dict_.get(sum_) != None:
                count = max(count,i-dict_.get(sum_))
            if dict_.get(sum_) == None:
                dict_[sum_] = i
        return count


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends