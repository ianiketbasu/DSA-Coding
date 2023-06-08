class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_map = {}
        li = []
        for num in nums :
            if num in my_map :
                my_map[num] += 1
            else :
                my_map[num] = 1
        
        for key,val in my_map.items() :
            if val > len(nums) / 3:
                li.append(key)
                
        return li