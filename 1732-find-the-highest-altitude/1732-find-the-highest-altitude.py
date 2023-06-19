class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = 0
        for i in range(0,len(gain)) :
            sum += gain[i]
            gain[i] = sum
        return max(0,max(gain))