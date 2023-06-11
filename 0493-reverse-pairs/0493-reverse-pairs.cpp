class Solution {
public:
    
    
    void mergeArray(vector<int>& nums,int low,int mid,int high){
        int left = low , right = mid + 1;
        vector<int> temp;
        while(left <= mid and right <= high){
            if(nums[left] <= nums[right]) 
                temp.push_back(nums[left++]);
            else 
                temp.push_back(nums[right++]);
        }
        
        while(left <= mid)
            temp.push_back(nums[left++]);
        while(right <= high)
            temp.push_back(nums[right++]);
        
        copy(temp.begin(),temp.end(),nums.begin() + low);
    }
    
    
    int countPair(vector<int>& nums,int low,int mid,int high){
        int ptr = mid + 1;
        int count = 0;
        for(int i=low;i<=mid;i++){
            while(ptr <= high and nums[i] > (nums[ptr] * 2LL)) ptr++;
            count += (ptr - (mid + 1));
        }
        
        return count;
    }
    
    
    int helper(vector<int>& nums,int low,int high) {
        int count = 0;
        if(low < high){
            int mid = (low + high)/2;
            count += helper(nums,low,mid);
            count += helper(nums,mid+1,high);
            count += countPair(nums,low,mid,high);
            mergeArray(nums,low,mid,high);
        }
        
        return count;
    }
    int reversePairs(vector<int>& nums) {
        return helper(nums,0,nums.size()-1);
    }
};