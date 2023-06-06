class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         my_set = set()
        
#         for num in nums :
#             if num in my_set:
#                 return num
#             else :
#                 my_set.add(num)
            
    
           # for mutable array
           # for i in range(0,len(nums)) :
           #      if nums[abs(nums[i])] < 0 :
           #          return abs(nums[i])
           #      else :
           #          nums[abs(nums[i])] = -nums[abs(nums[i])]
            
            slow , fast = nums[0] , nums[0]
            while True :
                slow = nums[slow]
                fast = nums[nums[fast]]
                if slow == fast :
                    break
            
            fast = nums[0]
            
            while slow != fast :
                slow = nums[slow]
                fast = nums[fast]
                
            return fast
            
