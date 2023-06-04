class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # n = len(nums)
        # li = []
        
        # for i in range(0,n-1) :
        #     for j in range(i+1,n) :
        #         if nums[i] + nums[j] == target :
        #             li.append(i)
        #             li.append(j)
        #             break
        # return li

        dict = {}

        for i in range(0,len(nums)) :
            key = target - nums[i]
            if dict.get(key) != None :
                return [dict.get(key),i]
            else:
                dict[nums[i]] = i