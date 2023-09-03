class Solution {
    public int maxSubArray(int[] nums) {
        int max_sum = Integer.MIN_VALUE;
        int temp = 0;
        for(int i=0;i<nums.length;i++){
            temp += nums[i];
            max_sum = Math.max(max_sum,temp);
            if(temp < 0)
                temp = 0;
        }
        return max_sum;
    }
}