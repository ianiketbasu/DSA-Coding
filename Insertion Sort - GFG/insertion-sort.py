#Sort the array using insertion sort

class Solution:
    def insert(self, alist, j, n):
        #code here
        while(j > 0 and alist[j-1] > alist[j]) :
            alist[j-1] , alist[j] = alist[j] , alist[j-1]
            j -= 1
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        for i in range(0,n) :
            j = i
            self.insert(alist,j,n)


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends