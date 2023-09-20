class Solution {
    public int minOperations(int[] nums, int x) {
        int total = 0;
        for (int element : nums) {
            total += element;
        }
        
        if(total == x) return nums.length;
        
        HashMap<Integer,Integer> map = new HashMap<>();
        int sum = 0;
        int ans = 0;
        int K = total - x;
        for(int i=0;i<nums.length;i++){
            sum += nums[i];
            if(sum == K) ans = i+1;
            else if(map.get(sum - K) != null) ans = Math.max(ans,i - map.get(sum-K));
            map.putIfAbsent(sum,i);
        }
        return ans == 0 ? -1 : nums.length - ans;
    }
}