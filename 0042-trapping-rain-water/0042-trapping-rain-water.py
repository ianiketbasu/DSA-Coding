class Solution:
    def trap(self, height: List[int]) -> int:
#         n = len(height)

#         if n < 3: 
#             return 0

#         leftMax = [0] * n
#         rightMax = [0] * n

#         lMax, rMax = height[0], height[n - 1]

#         for i in range(1, n - 1):
#             leftMax[i] = lMax
#             lMax = max(lMax, height[i])

#             rightMax[n - i - 1] = rMax
#             rMax = max(rMax, height[n - i - 1])
#         water = 0
#         for i in range(1,n-1) :
#             if height[i] < leftMax[i] and height[i] < rightMax[i] :
#                 water += min(leftMax[i],rightMax[i]) - height[i]
        
#         return water


#         water , level = 0 , 0
#         l , r = 0 , len(height) - 1
        
#         while l < r :
#             lower = height[l] if height[l] < height[r] else height[r]
#             level = max(lower,level)
            
#             water += level - lower
            
#             if height[l] < height[r] :
#                 l += 1
#             else :
#                 r -= 1
        
#         return water

            
        water = 0
        n = len(height)
        maxLeft , maxRight= height[0] , height[n-1]
        l , r = 1 , n-2
        
        while l <= r :
            if maxLeft < maxRight :
                if maxLeft < height[l] :
                    maxLeft = height[l]
                else :
                    water += maxLeft - height[l]
                l += 1
            else :
                if maxRight < height[r] :
                    maxRight = height[r]
                else :
                    water += maxRight - height[r]
                r -= 1
        
        return water
            
            