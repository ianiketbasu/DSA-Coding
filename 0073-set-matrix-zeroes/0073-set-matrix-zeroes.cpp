// class Solution {
//     void makeZero(pair<int,int> p,vector<vector<int>>& m){
//         int r = m.size() , c = m[0].size();
//         int x = p.first , y = p.second;
        
//         for(int j = y ; j <c ; j++) m[x][j] = 0;
//         for(int i = x ; i < r ; i++) m[i][y] = 0;
        
//         for(int j = y ; j >= 0 ; j--) m[x][j] = 0;
//         for(int i = x ; i >= 0 ; i--) m[i][y] = 0;
//     }
// public:
//     void setZeroes(vector<vector<int>>& m) {
//         vector<pair<int,int>> v;
//         for(int i=0;i<m.size();i++)
//             for(int j=0;j<m[0].size();j++)
//                 if(m[i][j] == 0) v.push_back({i,j});
        
//         for(pair<int,int> it : v) makeZero(it,m);
//     }
// };


class Solution {
public:
    void setZeroes(vector<vector<int>>& mat) {
  
        int row = mat.size() , col = mat[0].size();
//         vector<int> r(row,0) , c(col,0);
//         for(int i=0;i<row;i++){
//             for(int j=0;j<col;j++){
//                 if(mat[i][j] == 0){
//                     r[i] = 1;
//                     c[j] = 1;
//                 }
//             }
//         }
        
//         for(int i=0;i<row;i++){
//             for(int j=0;j<col;j++){
//                 if(r[i] or c[j]){
//                     mat[i][j] = 0;
//                 }
//             }
//         }
        int colZero = 1 ;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                
                if(mat[i][j] == 0){
                    mat[i][0] = 0;
                    if(j!=0) mat[0][j] = 0;
                    else colZero = 0;
                }
            }
        }

        for(int i=1;i<row;i++){
            for(int j=1;j<col;j++){
                if(mat[i][j] !=0){
                    if(mat[0][j] == 0 || mat[i][0] == 0) 
                    mat[i][j] = 0;
                }
            }
        }
    
        if(mat[0][0] == 0){
            for(int i=0;i<col;i++)
                mat[0][i] = 0;
        }
        if(colZero == 0){
            for(int i=0;i<row;i++){
                mat[i][0] = 0;
            }
        }
    
    
    
    
    
    }
        
        
         
        
            

};