class Solution {
    // int oneCount(vector<int> v){
    //     int n = 0;
    //     for(auto it : v) if(it == 1) n++;
    //     return n;
    // }
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        
//         vector<pair<int,int>> vec;
        vector<int> ans;
        
//         for(int i=0;i<mat.size();i++) vec.push_back({count(mat[i].begin(),mat[i].end(),1) , i});
        
//         sort(vec.begin(),vec.end());
      
//         for(int i=0;i<k;i++) ans.push_back(vec[i].second);
        
        
//         return ans;
        
        
        //min priority queue . . .
        priority_queue<pair<int,int> , vector<pair<int,int>> , greater<pair<int,int>>> pq;
        for(int i=0;i<mat.size();i++){
            vector<int> it = mat[i];
            int ans = upper_bound(it.rbegin(),it.rend(),0) - it.rbegin();
            pq.push({it.size()-ans,i});
        }
        while(k--){
            ans.emplace_back(pq.top().second);
            pq.pop();
        }
        return ans;
        
    }
};