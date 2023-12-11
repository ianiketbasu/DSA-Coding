class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        map<int,int> mpp;
        for(auto it : arr) mpp[it]++;
        int n = size(arr);
       
        for(auto it : mpp) {
            if(it.second > n/4) return it.first;
        }
    
        return 0;
    }
};