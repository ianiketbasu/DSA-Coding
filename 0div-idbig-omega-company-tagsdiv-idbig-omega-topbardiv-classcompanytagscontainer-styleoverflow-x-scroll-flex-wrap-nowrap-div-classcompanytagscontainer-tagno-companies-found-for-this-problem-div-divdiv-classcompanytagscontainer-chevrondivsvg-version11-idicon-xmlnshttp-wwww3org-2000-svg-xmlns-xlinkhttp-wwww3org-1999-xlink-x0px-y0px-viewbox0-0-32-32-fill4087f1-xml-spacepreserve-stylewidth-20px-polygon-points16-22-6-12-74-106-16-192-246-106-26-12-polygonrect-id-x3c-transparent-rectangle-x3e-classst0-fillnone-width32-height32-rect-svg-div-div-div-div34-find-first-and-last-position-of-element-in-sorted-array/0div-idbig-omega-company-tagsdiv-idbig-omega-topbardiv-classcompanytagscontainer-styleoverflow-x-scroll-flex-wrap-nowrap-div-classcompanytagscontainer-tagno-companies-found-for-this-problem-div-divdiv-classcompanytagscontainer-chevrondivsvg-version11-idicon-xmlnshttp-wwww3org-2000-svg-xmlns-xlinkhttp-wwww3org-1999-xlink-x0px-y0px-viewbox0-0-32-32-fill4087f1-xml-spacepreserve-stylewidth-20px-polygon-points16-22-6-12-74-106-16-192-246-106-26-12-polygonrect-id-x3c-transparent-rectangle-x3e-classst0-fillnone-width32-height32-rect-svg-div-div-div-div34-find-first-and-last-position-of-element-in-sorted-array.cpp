class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int x) {
        vector<int> res;
        
        //binary search
//         int low = 0 ,high = nums.size()-1,mid ,ans = -1;
//         while(low <= high){
//             mid = (low+high) /2;
//             if(nums[mid] > x) high = mid - 1;
//             else if(nums[mid] < x)low = mid + 1;
//             else{
//                 ans = mid;
//                 high = mid -1;
//             }
//         }
//         res.push_back(ans);
        
//         low = 0,high = nums.size()-1,ans = -1;
//         while(low <= high){
//             mid = (low+high) /2;
//             if(nums[mid] > x) high = mid - 1;
//             else if(nums[mid] < x)  low = mid + 1;
//             else{
//                 ans = mid;
//                 low = mid + 1;
//             }
//         }
//         res.push_back(ans);
//         return res;
        
        if(nums.size() < 1) return {-1,-1};
        int first = lower_bound(nums.begin(), nums.end(), x) - nums.begin();
        int last = (upper_bound(nums.begin(), nums.end(), x) - nums.begin()) - 1;
        if(first == nums.size()) return {-1,-1};
        if(nums[first] == x and nums[last] == x) return {first,last};
        return {-1,-1};

        
    }
};