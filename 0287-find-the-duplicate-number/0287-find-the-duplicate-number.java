class Solution {
    public int findDuplicate(int[] nums) {
        HashMap<Integer,Boolean> mpp = new HashMap<>();
        
        for(int i=0;i<nums.length;i++){
            if(mpp.containsKey(nums[i]) == true){
                return nums[i];
            }
            mpp.put(nums[i],true);
        }
        
        return 0;
    }
}