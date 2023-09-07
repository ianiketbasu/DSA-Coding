class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
//         Set<List<Integer>> mySet = new HashSet<>();
//         Arrays.sort(nums);
//         for(int i=0;i<nums.length;i++){
//             for(int j=i+1;j<nums.length;j++){
//                 for(int k=j+1;k<nums.length;k++){
//                     int sum = nums[i] + nums[j] + nums[k];
//                     if(sum == 0){
//                         List<Integer> triplet = new ArrayList<>();
//                         triplet.add(nums[i]);
//                         triplet.add(nums[j]);
//                         triplet.add(nums[k]);
//                         mySet.add(triplet);
//                     }
//                 }
//             }
//         }
        
//         List<List<Integer>> ans = new ArrayList<>();
        
//         for(List<Integer> triplet : mySet){
//             ans.add(triplet);
//         }
        
//         return ans;
        
        
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        
        for(int i=0;i<nums.length-2;i++){
            if(i == 0 || nums[i] != nums[i-1]){
                int low = i+1;
                int high = nums.length - 1;
                int sum = -nums[i];
                while(low < high){
                    if(nums[low] + nums[high] == sum){
//                         List<Integer> triplet = new ArrayList<>();
//                         triplet.add(nums[i]);
//                         triplet.add(nums[low]);
//                         triplet.add(nums[high]);
                        
//                         ans.add(triplet);
                        ans.add(Arrays.asList(nums[i], nums[low], nums[high]));
                        
                        while(low < high && nums[low] == nums[low+1]) low++;
                        while(low < high && nums[high] == nums[high-1]) high--;
                        
                        low++;
                        high--;
                    }
                    else if(nums[low] + nums[high] < sum) low++;
                    else high--;
                }
            }
        }
        
        return ans;
    }
}