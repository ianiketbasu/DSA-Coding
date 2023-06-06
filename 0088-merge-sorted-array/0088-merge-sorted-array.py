class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[:] = sorted(nums1[:m] + nums2[:n])
        i = n + m - 1
        ptr1 , ptr2 = m-1 , n-1
        
        while(ptr2 >= 0) :
            if ptr1>=0 and nums1[ptr1] > nums2[ptr2]:
                nums1[i] = nums1[ptr1]
                i -=1
                ptr1 -= 1
            
            else :
                nums1[i] = nums2[ptr2]
                i -= 1
                ptr2 -= 1
                
            
         