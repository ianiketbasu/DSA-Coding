class Solution {
public:
    int peakIndexInMountainArray(vector<int>& nums) {
//          int l = 0, r = nums.size() - 1;
        
//         while (l <= r) {
//             int mid = (l + r) >> 1;
//             if (nums[mid] < nums[mid + 1])
//                 l = mid + 1;
//             else
//                 r = mid - 1;
//         }
        
//         return l;
        
        return max_element(nums.begin(),nums.end()) - nums.begin();
    }
};