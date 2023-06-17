class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n < 3: 
            return 0

        leftMax = [0] * n
        rightMax = [0] * n

        lMax, rMax = height[0], height[n - 1]

        for i in range(1, n - 1):
            leftMax[i] = lMax
            lMax = max(lMax, height[i])

            rightMax[n - i - 1] = rMax
            rMax = max(rMax, height[n - i - 1])
        water = 0
        for i in range(1,n-1) :
            if height[i] < leftMax[i] and height[i] < rightMax[i] :
                water += min(leftMax[i],rightMax[i]) - height[i]
        
        return water