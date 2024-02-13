/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(n) {
    if(n === 1) return [[1]];
    else if(n === 2) return [[1],[1,1]];
    
    const ans = [[1],[1,1]];
    
    for(let i=2;i<n;++i){
        const temp = [1];
        for(let j=1;j<ans[i-1].length;j++){
            temp.push(ans[i-1][j] + ans[i-1][j-1]);
        }
        temp.push(1);
        ans.push(temp);
    }
    
    return ans;
};