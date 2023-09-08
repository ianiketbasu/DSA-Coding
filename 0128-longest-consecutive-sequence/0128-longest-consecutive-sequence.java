class Solution {
    public int longestConsecutive(int[] nums) {
        
//         if(nums.length == 1) return 1;
//         if(nums.length == 0) return 0;
//         Arrays.sort(nums);
//         int count = 1;
//         int max_len = count;
        

//         for(int i=1;i<nums.length;i++){
//             while(i < nums.length && nums[i] == nums[i-1]) i++;
//             if(i < nums.length && nums[i] == nums[i-1] + 1){
//                 count++;
//                 max_len = Math.max(max_len , count);
//             }
//             else{
//                 count = 1;
//             }
//         }
        
//         return max_len;
        
        
        Set<Integer> mySet = new HashSet<>();
        int max_len = 0;
        for(int i=0;i<nums.length;i++) mySet.add(nums[i]);
        for(int num : mySet){
            if(!mySet.contains(num - 1)){
                int y = num + 1;
                while(mySet.contains(y)) y++;
                max_len = Math.max(max_len,y-num);
            }
        }
        return max_len;
    }
}