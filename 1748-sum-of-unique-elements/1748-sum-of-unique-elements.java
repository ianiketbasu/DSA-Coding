class Solution {
    public int sumOfUnique(int[] nums) {
        Map<Integer,Integer> my_map = new HashMap<>();
        
        for(int i=0;i<nums.length;i++){
            if(my_map.containsKey(nums[i])){
                my_map.put(nums[i],my_map.get(nums[i]) + 1);
            }
            else{
                my_map.put(nums[i],1);
            }
        }
        
        int sum = 0;
        
        for(int i=0;i<nums.length;i++){
            if(my_map.get(nums[i]) == 1){
                sum += nums[i];
            }
        }
        return sum;
    }
}