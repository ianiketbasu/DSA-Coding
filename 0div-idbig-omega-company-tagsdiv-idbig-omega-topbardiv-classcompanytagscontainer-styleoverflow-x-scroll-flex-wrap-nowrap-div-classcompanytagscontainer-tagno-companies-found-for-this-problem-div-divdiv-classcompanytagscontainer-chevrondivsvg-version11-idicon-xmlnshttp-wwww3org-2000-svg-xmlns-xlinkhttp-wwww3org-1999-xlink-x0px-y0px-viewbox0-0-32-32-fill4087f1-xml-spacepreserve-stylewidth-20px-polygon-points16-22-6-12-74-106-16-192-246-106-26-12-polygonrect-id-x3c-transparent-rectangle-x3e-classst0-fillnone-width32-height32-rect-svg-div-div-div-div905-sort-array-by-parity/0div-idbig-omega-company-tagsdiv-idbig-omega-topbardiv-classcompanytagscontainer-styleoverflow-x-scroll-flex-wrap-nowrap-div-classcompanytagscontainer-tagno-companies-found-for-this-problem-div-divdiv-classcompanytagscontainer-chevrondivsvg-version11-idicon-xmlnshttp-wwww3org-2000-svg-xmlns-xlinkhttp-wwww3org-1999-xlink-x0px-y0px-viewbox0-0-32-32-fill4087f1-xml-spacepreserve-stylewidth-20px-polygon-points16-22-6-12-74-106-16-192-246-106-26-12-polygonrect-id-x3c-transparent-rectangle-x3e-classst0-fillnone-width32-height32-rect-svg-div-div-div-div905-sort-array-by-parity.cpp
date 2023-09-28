class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
//         int s = 0 , e = nums.size() - 1 ;
        
//         while(s < e){
//             if(nums[s] % 2 != 0 and nums[e] % 2 == 0) swap(nums[s++],nums[e--]);
//             else if(nums[s] % 2 == 0) s++;
//             else if(nums[s] % 2 != 0 and nums[e] % 2 != 0) e--;
//         }
//         return nums;
        
        for(int i = 0 , j = 0 ; j < nums.size() ; j++) if(nums[j] % 2 == 0) swap(nums[i++] , nums[j]);
        return nums;
    }
};