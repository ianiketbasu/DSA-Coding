class Solution {
public:
    int minSubArrayLen(int t, vector<int>& nums) {
        int n = size(nums);
        int left = 0 , right = 0;
        int ans = INT_MAX;
        int sum = 0;
        while(right < n){
            sum += nums[right];
            if(sum >= t){
                while(sum >= t) sum -= nums[left++];
                ans = min(ans,right-left+2);
                
            }
            right++;
        }
        return ans == INT_MAX ? 0 : ans ;
        
    }
};