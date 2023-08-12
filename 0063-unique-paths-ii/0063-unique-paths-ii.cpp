class Solution {
    // Recursive Function
    // int helper(int m,int n,int x,int y,vector<vector<int>>& vec){
    //     if(x == m-1 and y == n-1) return 1;
    //     if(x >= m or y >= n or vec[x][y] == 1) return 0;
    //     return helper(m,n,x+1,y,vec) + helper(m,n,x,y+1,vec);
    // }
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        //if the obstacle is placed in the destination then there is no possible path . . . 
    //     if(obstacleGrid[m-1][n-1] == 1) return 0;
    //     return helper(m,n,0,0,obstacleGrid);
        
        
        
        //boundary case
        
        if(obstacleGrid[m-1][n-1] == 1) return 0;
        vector<vector<int>> dp(m,vector<int>(n,0));
        
        for(int i=0;i<m;i++)
            if(obstacleGrid[i][0] == 1) break;
            else dp[i][0] = 1;
        for(int j=0;j<n;j++)
            if(obstacleGrid[0][j] == 1) break;
            else dp[0][j] = 1;
        
        for(int i=1;i<m;i++)
            for(int j=1;j<n;j++)
                if(obstacleGrid[i][j] == 1) dp[i][j] = 0;
                else dp[i][j] = dp[i-1][j] + dp[i][j-1];
        
        return dp[m-1][n-1];
    }
};