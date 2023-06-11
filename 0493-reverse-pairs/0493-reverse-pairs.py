class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def merge(nums, low, mid, high):
            left = low
            right = mid + 1
            li = []
            count = 0
            
            ptr = mid + 1
            for i in range(low,mid+1) :
                while ptr <= high and nums[i] > 2*nums[ptr] : ptr += 1
                count += (ptr - (mid + 1))
            

            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    li.append(nums[left])
                    left += 1
                else:
                    li.append(nums[right])
                    right += 1

            while left <= mid:
                li.append(nums[left])
                left += 1

            while right <= high:
                li.append(nums[right])
                right += 1

            nums[low:high + 1] = li

            return count

            
            
            
        def getPairCount(nums,low,high) :
            count = 0
            if low < high :
                mid = (low + high) // 2
                count += getPairCount(nums,low,mid)
                count += getPairCount(nums,mid+1,high)
                
                count += merge(nums,low,mid,high)
            
            return count
        
        
        
        
        
        return getPairCount(nums,0,len(nums)-1)
        