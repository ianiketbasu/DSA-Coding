class Solution(object):
    def nextPermutation(self,nums):
        n = len(nums)
        if n == 1:
            return

        last_inc = -1
        i = 1
        while i < n:
            if nums[i] > nums[i-1]:
                last_inc = i
            i += 1

        if last_inc == -1:
            nums.reverse()
            return

        last_inc_val = nums[last_inc]
        index = last_inc
        for i in range(last_inc, n):
            if nums[i] > nums[last_inc-1]:
                index = i

        nums[last_inc-1], nums[index] = nums[index], nums[last_inc-1]
        nums[last_inc:] = sorted(nums[last_inc:])

      


