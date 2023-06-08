class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
# #         my_map = {}
#         li = []
#         for num in nums :
#             if num in my_map :
#                 my_map[num] += 1
#             else :
#                 my_map[num] = 1
        
#         for key,val in my_map.items() :
#             if val > len(nums) / 3:
#                 li.append(key)
                
#         return li


#         counter1 , counter2 , ele1 , ele2 = 0 ,0 , None , None
        
#         for num in nums :
#             if counter1 == 0 and num != ele2 :
#                 ele1 = num
#                 counter1 += 1
#             elif counter2 == 0 and num != ele1 :
#                 ele2 = num
#                 counter2 += 1
#             elif num == ele1 :
#                 counter1 += 1
#             elif num == ele2 :
#                 counter2 += 1
#             else :
#                 counter1 -= 1
#                 counter2 -= 1
        
#         counter1 , counter2 = 0 , 0
#         for num in nums :
#             if ele1 == num :
#                 counter1 += 1
#             elif ele2 == num :
#                 counter2 += 1
#         li = []  
#         if counter1 > len(nums) / 3 :
#             li.append(ele1)
#         if counter2 > len(nums) / 3 :
#             li.append(ele2)
        
#         return li

        # return [n for n in set(nums) if nums.count(n) > len(nums) / 3]

    
    def majorityElement(self, nums):
        ctr = collections.Counter()
        for n in nums:
            # print("for ",n," : ---------")
            ctr[n] += 1
            # print("=======")
            # print(ctr)
            # print("=======")
            if len(ctr) == 3:
                # print("------")
                # print(ctr)
                
                ctr -= collections.Counter(set(ctr))
                
        #         print(ctr)
        #         print("------")
        #     print("end of loop\n\n")
        # print(ctr)
        return [n for n in ctr if nums.count(n) > len(nums)/3]



