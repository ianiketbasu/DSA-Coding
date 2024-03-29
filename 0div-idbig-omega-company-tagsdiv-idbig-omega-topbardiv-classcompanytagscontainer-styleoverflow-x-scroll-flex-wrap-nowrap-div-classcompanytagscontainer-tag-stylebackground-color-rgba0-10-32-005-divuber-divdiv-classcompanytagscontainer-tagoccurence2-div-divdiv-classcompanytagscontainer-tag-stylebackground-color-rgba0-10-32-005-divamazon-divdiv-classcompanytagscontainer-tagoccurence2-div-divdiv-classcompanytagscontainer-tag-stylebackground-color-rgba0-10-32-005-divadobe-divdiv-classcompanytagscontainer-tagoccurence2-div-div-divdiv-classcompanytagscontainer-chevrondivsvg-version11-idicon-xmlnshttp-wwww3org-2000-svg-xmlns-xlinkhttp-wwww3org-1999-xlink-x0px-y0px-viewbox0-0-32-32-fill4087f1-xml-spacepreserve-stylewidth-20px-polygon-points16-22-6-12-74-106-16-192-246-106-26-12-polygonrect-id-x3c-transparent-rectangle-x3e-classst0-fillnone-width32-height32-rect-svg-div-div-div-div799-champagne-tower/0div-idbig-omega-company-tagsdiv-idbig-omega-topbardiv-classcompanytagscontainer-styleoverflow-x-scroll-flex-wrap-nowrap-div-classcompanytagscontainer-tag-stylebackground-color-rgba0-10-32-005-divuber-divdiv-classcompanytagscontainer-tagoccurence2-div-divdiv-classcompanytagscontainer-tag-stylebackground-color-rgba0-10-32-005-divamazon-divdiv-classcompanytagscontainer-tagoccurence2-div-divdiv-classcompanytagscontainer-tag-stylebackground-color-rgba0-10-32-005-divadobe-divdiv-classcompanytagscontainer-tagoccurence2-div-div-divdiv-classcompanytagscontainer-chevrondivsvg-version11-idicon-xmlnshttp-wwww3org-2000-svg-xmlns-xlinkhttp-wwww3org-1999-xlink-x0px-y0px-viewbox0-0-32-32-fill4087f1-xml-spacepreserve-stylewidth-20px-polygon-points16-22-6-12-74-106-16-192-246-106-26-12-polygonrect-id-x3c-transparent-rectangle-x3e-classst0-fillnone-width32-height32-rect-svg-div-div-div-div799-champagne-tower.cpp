class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        double dp[101][101] = {0.0};
        dp[0][0] = poured;
        
        for(int i=0;i<query_row;i++){
            for(int j=0;j<=i;j++){
                double flow = (dp[i][j] - 1) /2.0;
                if(flow > 0){
                    dp[i+1][j] += flow;
                    dp[i+1][j+1] += flow;
                }
            }
        }
        return min(1.0,dp[query_row][query_glass]);
    }
};