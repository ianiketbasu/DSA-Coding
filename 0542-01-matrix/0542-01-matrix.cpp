class Solution {
    bool isValid(int i,int j,int r,int c){
        if(i<0 or j<0 or i>=r or j>=c) return false;
        return true;
    }
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int r = mat.size() , c = mat[0].size();
        queue<pair<int,int>> q;
        vector<vector<int>> ans(r,vector<int>(c,-1));
        
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(mat[i][j] == 0){
                    q.push({i,j});
                    ans[i][j] = 0;
                }
            }
        }
        
        //BFS Call
        while(!q.empty()){
            int i = q.front().first;
            int j = q.front().second;
            
            q.pop();
            
            if(isValid(i+1,j,r,c) and ans[i+1][j] == -1){
                q.push({i+1,j});
                ans[i+1][j] = ans[i][j] + 1;
            }
            if(isValid(i-1,j,r,c) and ans[i-1][j] == -1){
                q.push({i-1,j});
                ans[i-1][j] = ans[i][j] + 1;
            }
            if(isValid(i,j+1,r,c) and ans[i][j+1] == -1){
                q.push({i,j+1});
                ans[i][j+1] = ans[i][j] + 1;
            }
            if(isValid(i,j-1,r,c) and ans[i][j-1] == -1){
                q.push({i,j-1});
                ans[i][j-1] = ans[i][j] + 1;
            }
            
        }
        return ans;
        
    }
};