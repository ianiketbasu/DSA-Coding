class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = size(nums);
        if(n < 3) return false;
        //O(n^3) approach (TLE)
        // for(int i = 0 ; i < n ; i++){
        //     for(int j = i + 1 ; j < n ; j++){
        //         for(int k = j + 1 ; k < n ; k++){
        //             if(nums[k] > nums[i] && nums[j] > nums[k]) return true;
        //         }
        //     }
        // }
        
        // O(n^2) approach (TLE)
        // int mini = nums[0];
        // for(int i = 1 ; i < n ; i++){
        //     for(int j = i + 1 ; j < n ; j++){
        //         if(nums[j] > mini and nums[i] > nums[j]) return true;
        //         mini = min(mini,nums[i]);
        //     }
        // }
        // return false;
        
        // O(2n)
//         stack<int> st;
//         vector<int> mini(n,nums[0]);
//         for(int i = 1 ; i < n ; i++)
//             mini[i] = min(nums[i],mini[i-1]);
        
//         for(int j = n-1 ; j >= 0 ; j--){
//             if(nums[j] > mini[j]){
//                 while(!st.empty() and st.top() <= mini[j]) st.pop();
//                 if(!st.empty() and st.top() < nums[j]) return true;
//                 st.push(nums[j]);
//             }
//         }
//         return false;
        
        // O(n)
        
        stack<int> st;
        int thirdEle = INT_MIN;
        for(int j = n-1 ; j >=0 ; j--){
            if(nums[j] < thirdEle) return true;
            while(!st.empty() and nums[j] > st.top()) {
                thirdEle = st.top();
                st.pop();
            }
            st.push(nums[j]);
        }
        return false;
        
    }
};