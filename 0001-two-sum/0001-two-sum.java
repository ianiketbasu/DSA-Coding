class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> mpp = new HashMap<>();

        
        for(int i=0;i<nums.length;i++){
            int val = target - nums[i];
            
            if(mpp.containsKey(val))
                return new int[] {mpp.get(val),i};
            mpp.put(nums[i],i);
        }
        
        return new int[] {-1,-1};
    }
}