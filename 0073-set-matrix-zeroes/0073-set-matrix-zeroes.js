/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(mat) {
        const row = mat.length;
        const col = mat[0].length;

        const r = new Array(row).fill(0);
        const c = new Array(col).fill(0);

        for(let i=0;i<row;i++){
            for(let j=0;j<col;j++){
                if(mat[i][j] == 0){
                    r[i] = 1;
                    c[j] = 1;
                }
            }
        }

        for(let i=0;i<row;i++){
            for(let j=0;j<col;j++){
                if(r[i] || c[j]){
                    mat[i][j] = 0;
                }
            }
        }
};