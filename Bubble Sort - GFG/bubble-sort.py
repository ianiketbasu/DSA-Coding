#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        isSwap = False
        for i in range(n-1,0,-1):
            for j in range(0,i):
                if arr[j] > arr[j+1] :
                    arr[j] , arr[j+1] = arr[j+1] , arr[j]
                    isSwap = True
            
            if isSwap == False :
                break
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends