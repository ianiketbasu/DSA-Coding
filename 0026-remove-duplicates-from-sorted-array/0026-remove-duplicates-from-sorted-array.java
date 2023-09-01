class Solution {
    public int removeDuplicates(int[] nums) {
        int i=0,j=0;
        for(j = i + 1;j<nums.length;j++){
            if(nums[i] != nums[j]){
                nums[i+1] = nums[j];
                ++i;
            }
        }
        
        return ++i;
    }
}