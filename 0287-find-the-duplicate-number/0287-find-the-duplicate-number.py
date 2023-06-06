class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_set = set()
        
        for num in nums :
            if num in my_set:
                return num
            else :
                my_set.add(num)