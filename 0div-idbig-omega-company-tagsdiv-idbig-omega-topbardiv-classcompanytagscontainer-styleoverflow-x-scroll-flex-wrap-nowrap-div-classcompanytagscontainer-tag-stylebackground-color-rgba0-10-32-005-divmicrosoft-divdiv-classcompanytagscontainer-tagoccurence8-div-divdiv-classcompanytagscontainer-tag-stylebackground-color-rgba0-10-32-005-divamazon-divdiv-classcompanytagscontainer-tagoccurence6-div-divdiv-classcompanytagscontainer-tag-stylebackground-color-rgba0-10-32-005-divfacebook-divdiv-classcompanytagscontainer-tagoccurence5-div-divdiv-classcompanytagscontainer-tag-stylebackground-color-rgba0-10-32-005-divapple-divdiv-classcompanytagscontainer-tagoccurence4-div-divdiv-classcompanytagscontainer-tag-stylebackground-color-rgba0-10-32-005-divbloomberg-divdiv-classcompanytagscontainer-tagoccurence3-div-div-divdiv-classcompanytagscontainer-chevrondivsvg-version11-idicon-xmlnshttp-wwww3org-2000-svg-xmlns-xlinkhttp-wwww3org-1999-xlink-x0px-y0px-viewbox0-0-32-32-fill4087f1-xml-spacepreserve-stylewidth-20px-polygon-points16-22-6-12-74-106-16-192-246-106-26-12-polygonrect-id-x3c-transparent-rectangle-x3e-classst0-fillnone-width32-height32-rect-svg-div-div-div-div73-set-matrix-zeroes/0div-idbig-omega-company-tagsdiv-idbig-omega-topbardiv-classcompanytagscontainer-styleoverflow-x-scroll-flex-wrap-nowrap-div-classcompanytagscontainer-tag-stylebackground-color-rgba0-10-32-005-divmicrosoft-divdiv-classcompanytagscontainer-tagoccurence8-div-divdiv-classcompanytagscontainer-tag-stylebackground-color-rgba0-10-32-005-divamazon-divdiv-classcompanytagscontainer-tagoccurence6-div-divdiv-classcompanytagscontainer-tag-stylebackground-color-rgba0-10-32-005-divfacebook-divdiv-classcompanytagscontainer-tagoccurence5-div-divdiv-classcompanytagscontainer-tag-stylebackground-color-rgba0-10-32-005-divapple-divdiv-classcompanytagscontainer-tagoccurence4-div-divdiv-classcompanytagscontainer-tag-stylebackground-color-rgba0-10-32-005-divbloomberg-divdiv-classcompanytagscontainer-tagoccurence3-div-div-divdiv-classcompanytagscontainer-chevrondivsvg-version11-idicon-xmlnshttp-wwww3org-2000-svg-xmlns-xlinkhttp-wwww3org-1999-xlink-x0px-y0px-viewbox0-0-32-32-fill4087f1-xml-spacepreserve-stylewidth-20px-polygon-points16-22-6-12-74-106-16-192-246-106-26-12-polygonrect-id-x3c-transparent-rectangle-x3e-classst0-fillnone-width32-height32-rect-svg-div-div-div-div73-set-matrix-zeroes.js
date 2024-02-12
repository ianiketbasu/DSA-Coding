/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const rows = matrix.length;
    const cols = matrix[0].length;
    
    const r = Array(rows).fill(1);
    const c = Array(cols).fill(1);
    
    for(let i=0;i<rows;i++){
        for(let j=0;j<cols;j++){
            if(matrix[i][j] === 0){
                r[i] = 0;
                c[j] = 0;
            }
        }
    }
    
    for(let i=0;i<rows;i++){
        for(let j=0;j<cols;j++){
            if(r[i] === 0 || c[j] === 0){
                matrix[i][j] = 0;
            }
        }
    }
    
    
};