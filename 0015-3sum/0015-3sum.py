class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # my_set = set()
        
        # for i in range(0,len(nums) - 2) :
        #     for j in range(i+1,len(nums) - 1) :
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0 :
        #                 li = [nums[i] , nums[j] , nums[k]]
        #                 li[:] = sorted(li)
        #                 my_set.add(tuple(li))
        # return list(my_set)
        
        ans = []
        nums[:] = sorted(nums)
        
        for i in range(0,len(nums)) :
            if i > 0 and nums[i] == nums[i-1] :
                continue
            j , k = i + 1 , len(nums) - 1
            while j < k :
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ < 0 :
                    j += 1
                elif sum_ > 0 :
                    k -= 1
                else :
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j] : 
                        j += 1
                    while j < k and nums[k+1] == nums[k] : 
                        k -= 1
            
        return ans
          