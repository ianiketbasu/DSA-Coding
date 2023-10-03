class Solution {
    public int numIdenticalPairs(int[] nums) {
        int cnt = 0 , arr[] = new int[101];
        for(int n : nums){
            cnt += arr[n]++;
        }
        return cnt;
    }
}