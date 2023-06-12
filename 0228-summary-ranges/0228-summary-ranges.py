class Solution:
    def getRange(self,start:int,end:int) -> int :
        if start == end :
            return str(start)
        else :
            result = str(start) + "->" + str(end)
            return result
        
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0 : return []
        start , end = nums[0] , nums[0]
        ans = []
        
        for i in range(1,n) :
            if nums[i] - 1 == end :
                end = nums[i]
            else :
                result = self.getRange(start,end)
                ans.append(result)
                start , end = nums[i] , nums[i]
        
        result = self.getRange(start,end)
        ans.append(result)    
        return ans