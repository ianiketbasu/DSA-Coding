class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0 , sum = 0;
        HashMap<Integer,Integer> mpp = new HashMap<>();
        
        for(int i=0;i<nums.length;i++){
            sum += nums[i];
            if(sum == k) count += 1;
            if(mpp.get(sum - k) != null) count += mpp.get(sum - k);
            mpp.put(sum,mpp.getOrDefault(sum,0)+1);
        }
        return count;
    }
}