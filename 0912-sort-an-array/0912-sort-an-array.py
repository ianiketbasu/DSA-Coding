class Solution:
    def mergeArray(self,nums:List[int],low:int,mid:int,high:int) -> None :
        temp = []
        left , right = low , mid + 1
        while left <= mid and right <= high:
            if nums[left] <= nums[right] :
                temp.append(nums[left])
                left += 1
            else :
                temp.append(nums[right])
                right += 1
        
        while left <= mid :
            temp.append(nums[left])
            left += 1
        
        while right <= high :
            temp.append(nums[right])
            right += 1
        
        nums[low:high+1] = temp
        
        
            
            
            
    def mergeSortAlgo(self,nums:List[int],low:int,high:int) -> None :
        # Base Condition
        if low >= high : 
            return
        
        mid = (low+high)//2
        
        self.mergeSortAlgo(nums,low,mid)
        self.mergeSortAlgo(nums,mid+1,high)
        
        self.mergeArray(nums,low,mid,high)
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSortAlgo(nums,0,len(nums)-1)
        return nums