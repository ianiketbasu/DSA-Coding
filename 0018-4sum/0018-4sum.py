class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums[:] = sorted(nums)
        
        for i in range(0,len(nums)) :
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)) :
                if j > i+1 and nums[j] == nums[j-1]:
                    continue                   
                k , l = j + 1 , len(nums) - 1
                while k < l :
                    sum_ = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum_ < target :
                        k += 1
                    elif sum_ > target :
                        l -= 1
                    else :
                        ans.append([nums[i] , nums[j] , nums[k] , nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k-1] == nums[k] : k+= 1
                        while k < l and nums[l+1] == nums[l] : l-=1
        return ans
