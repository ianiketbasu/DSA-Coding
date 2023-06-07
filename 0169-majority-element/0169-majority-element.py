# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         my_map = {}
        
#         for num in nums :
#             if num in my_map :
#                 my_map[num] += 1
#             else :
#                 my_map[num] = 1
#         ans = None
#         count = float('-inf')
        
#         for key,value in my_map.items() :
#             if value > count :
#                 ans = key
#                 count = value
        
#         return ans

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # my_map = {}
        # for num in nums :
        #     my_map[num] = my_map.get(num , 0) + 1
        #     if my_map[num] > len(nums)/2 :
        #         return num
        
        ele , count = None,0
        for num in nums :
            if count == 0 :
                count = 1
                ele = num
            
            elif num == ele :
                count += 1
            
            else :
                count -= 1

        
        return ele