class Solution {
    public int findDuplicate(int[] nums) {
//         HashMap<Integer,Boolean> mpp = new HashMap<>();
        
//         for(int i=0;i<nums.length;i++){
//             if(mpp.containsKey(nums[i]) == true){
//                 return nums[i];
//             }
//             mpp.put(nums[i],true);
//         }
        
//         return 0;
        
        
        // HashSet<Integer> hs = new HashSet<>();
        
        // for(int num : nums){
        //     if(hs.contains(num)){
        //         return num;
        //     }
        //     hs.add(num);
        // }
        
        // return 0;

        int slow = nums[0], fast = nums[0];
         do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        fast = nums[0];
        while(slow != fast){
            slow = nums[slow];
            fast = nums[fast];
        }

        return fast;
    }
}