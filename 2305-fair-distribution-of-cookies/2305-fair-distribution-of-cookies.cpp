class Solution {
public:
    int ans = INT_MAX;
    void helper(vector<int>& c,vector<int>& b,int i,int k){
        if(i == c.size()){
            int ele = INT_MIN;
            for(auto it : b) ele = max(ele,it);
            ans = min(ans,ele);
            return;
        }
        for(int j=0;j<k;++j){
            b[j] += c[i];
            helper(c,b,i+1,k);
            b[j] -= c[i];
        }
    }
    int distributeCookies(vector<int>& c, int k) {
        vector<int> bags(k,0);
        helper(c,bags,0,k);
        return ans;
    }
};