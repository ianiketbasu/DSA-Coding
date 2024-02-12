/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const rows = matrix.length;
    const cols = matrix[0].length;
    
//     const r = Array(rows).fill(1);
//     const c = Array(cols).fill(1);
    
//     for(let i=0;i<rows;i++){
//         for(let j=0;j<cols;j++){
//             if(matrix[i][j] === 0){
//                 r[i] = 0;
//                 c[j] = 0;
//             }
//         }
//     }
    
//     for(let i=0;i<rows;i++){
//         for(let j=0;j<cols;j++){
//             if(r[i] === 0 || c[j] === 0){
//                 matrix[i][j] = 0;
//             }
//         }
//     }
    let firstRowHasZero = false;
    let firstColHasZero = false;
    for(let i=0;i<cols;i++){
        if(matrix[0][i] === 0){
            firstRowHasZero = true;
            break;
        }
    }
    
    for(let j=0;j<rows;j++){
       if(matrix[j][0] === 0){
           firstColHasZero = true;
           break;
       }
    }
    
    for(let i=1;i<rows;i++){
        for(let j=1;j<cols;j++){
            if(matrix[i][j] === 0){
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }
    for(let i=1;i<rows;i++){
        for(let j=1;j<cols;j++){
            if(matrix[0][j] === 0 || matrix[i][0] === 0){
                matrix[i][j] = 0;
            }
        }
    }
    
    
    if(firstRowHasZero){
        for(let i=0;i<cols;i++){
            matrix[0][i] = 0;
        }
    }
    if(firstColHasZero){
        for(let j=0;j<rows;j++){
            matrix[j][0] = 0;
        }
    }
    
};