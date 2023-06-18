class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count , curr_count = 0 ,  0
        for num in nums :
            if num :
                curr_count += 1
                max_count = max(max_count,curr_count)
            else :
                curr_count = 0
        return max_count