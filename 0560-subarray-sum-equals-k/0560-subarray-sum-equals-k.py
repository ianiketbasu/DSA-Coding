# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         count , sum_ = 0 , 0
#         my_map = defaultdict(int)
        
#         for num in nums :
#             sum_ += num
#             if sum_ == k :
#                 count += 1
#             if (sum_ - k) in my_map :
#                 count += my_map[sum_ - k]
                
#             my_map[sum_]+=1
            
#         return count
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count , sum_ = 0 , 0
        counter = Counter()

        for num in nums :
            sum_ += num
            if sum_ == k :
                count += 1
            if counter[sum_ - k] != 0 :
                count += counter[sum_ - k]
            counter[sum_] += 1
                
        return count
