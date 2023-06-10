#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        mini_idx = i
        for j in range(i,n):
            if arr[mini_idx] > arr[j] :
                mini_idx = j
        
        return mini_idx
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1) :
            mini_idx = self.select(arr,i)
            arr[i] , arr[mini_idx] = arr[mini_idx] , arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends