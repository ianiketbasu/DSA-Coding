class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        if(matches.size() == 1) return {{matches[0][0]} , {matches[0][1]}};
        
        vector<vector<int>> ans(2);
        vector<int> win(100001,0);
        vector<int> lose(100001,0);
        
        for(auto it : matches){
            win[it[0]]++;
            lose[it[1]]++;
        }
        
        vector<int> winP;
        for(int i=0 ; i < 100001; i++ )
            if(win[i] >= 1 and lose[i] == 0) winP.emplace_back(i);
        
        sort(winP.begin(),winP.end());
        
        vector<int> loseP;
        for(int i=0 ; i< 100001;i++)
            if(lose[i] == 1) loseP.emplace_back(i);
        
        sort(loseP.begin(),loseP.end());
        
        ans[0] = winP;
        ans[1] = loseP;
        
        return ans;
    }
};