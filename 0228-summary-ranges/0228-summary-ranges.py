class Solution:
    # def getRange(self,start:int,end:int) -> int :
    #     if start == end :
    #         return str(start)
    #     else :
    #         result = str(start) + "->" + str(end)
    #         return result
        
    def summaryRanges(self, nums: List[int]) -> List[str]:
#         n = len(nums)
#         if n == 0 : return []
#         start , end = nums[0] , nums[0]
#         ans = []
        
#         for i in range(1,n) :
#             if nums[i] - 1 == end :
#                 end = nums[i]
#             else :
#                 result = self.getRange(start,end)
#                 ans.append(result)
#                 start , end = nums[i] , nums[i]
        
#         result = self.getRange(start,end)
#         ans.append(result)    
#         return ans
    
    
    
            res = []
            for i in nums:
                if res and res[-1][1] == i-1:
                    res[-1][1] = i
                else:
                    res.append([i,i])
            return [str(x)+"->"+str(y) if x!=y else str(x) for x,y in res]
            
            
            
            # ranges = []
            # for n in nums:
            #     if not ranges or n > ranges[-1][-1] + 1:
            #         ranges += [],
            #     ranges[-1][1:] = n,
            #     print(ranges)
            # return ['->'.join(map(str, r)) for r in ranges]