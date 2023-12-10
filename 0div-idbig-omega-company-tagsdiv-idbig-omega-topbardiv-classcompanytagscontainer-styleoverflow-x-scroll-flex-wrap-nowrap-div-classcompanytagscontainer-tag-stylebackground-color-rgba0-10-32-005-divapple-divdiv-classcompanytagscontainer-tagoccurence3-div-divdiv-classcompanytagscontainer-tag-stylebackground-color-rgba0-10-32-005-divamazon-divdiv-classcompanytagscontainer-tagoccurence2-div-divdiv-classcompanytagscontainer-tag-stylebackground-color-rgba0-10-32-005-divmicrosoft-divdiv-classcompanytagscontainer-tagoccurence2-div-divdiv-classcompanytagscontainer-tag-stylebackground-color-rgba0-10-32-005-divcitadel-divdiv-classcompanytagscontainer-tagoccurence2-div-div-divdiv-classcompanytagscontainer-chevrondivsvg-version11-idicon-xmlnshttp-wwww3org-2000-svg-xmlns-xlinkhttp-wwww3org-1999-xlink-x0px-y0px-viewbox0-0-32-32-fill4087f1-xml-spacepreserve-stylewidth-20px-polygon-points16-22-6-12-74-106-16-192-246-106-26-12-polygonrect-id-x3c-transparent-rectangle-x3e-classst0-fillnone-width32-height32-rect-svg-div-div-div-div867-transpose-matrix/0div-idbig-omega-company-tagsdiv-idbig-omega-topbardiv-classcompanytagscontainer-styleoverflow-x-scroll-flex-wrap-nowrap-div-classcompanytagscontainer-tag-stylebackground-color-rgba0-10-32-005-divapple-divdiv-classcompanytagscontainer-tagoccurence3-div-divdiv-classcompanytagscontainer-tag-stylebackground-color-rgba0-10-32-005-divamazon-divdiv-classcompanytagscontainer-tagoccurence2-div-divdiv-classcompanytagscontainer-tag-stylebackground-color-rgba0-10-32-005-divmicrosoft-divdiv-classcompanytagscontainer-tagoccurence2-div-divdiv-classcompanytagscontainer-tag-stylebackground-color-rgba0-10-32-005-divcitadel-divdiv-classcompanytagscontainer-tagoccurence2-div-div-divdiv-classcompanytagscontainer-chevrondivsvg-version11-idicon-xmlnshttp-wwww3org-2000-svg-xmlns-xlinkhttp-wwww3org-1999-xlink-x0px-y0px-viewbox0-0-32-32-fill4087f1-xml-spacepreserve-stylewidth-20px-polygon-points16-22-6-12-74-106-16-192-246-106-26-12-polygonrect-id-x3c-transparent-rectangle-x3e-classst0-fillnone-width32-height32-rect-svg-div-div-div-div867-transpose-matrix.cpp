class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int r = matrix.size() , c = matrix[0].size();
        vector<vector<int>> ans(c,vector<int>(r));
        
        for(int j = 0 ; j < c ; j++)
            for(int i = 0 ; i < r ; i++)
                ans[j][i] = matrix[i][j];
        
        return ans;
    }
};