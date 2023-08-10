class Solution {
public:
    bool search(vector<int>& nums, int target) {
        // for(auto it : nums) if (it == target) return true;
        // return false;
        
        int low = 0;
        int high = nums.size() - 1;
        int mid;
        while(low <= high){
            mid = (low + high) / 2;
            if(nums[mid] == target) return true;
            if(nums[low] == nums[mid] and nums[mid] == nums[high]) {
                low++;
                high--;
            }
            else if(nums[mid] >= nums[low]){
                if(target <= nums[mid] and target >= nums[low]) high = mid - 1;
                else low = mid + 1;
            }
            else{
                if(target >= nums[mid] and target <= nums[high]) low = mid + 1;
                else high = mid - 1;
            }
        }
        
        return false;
    }
};