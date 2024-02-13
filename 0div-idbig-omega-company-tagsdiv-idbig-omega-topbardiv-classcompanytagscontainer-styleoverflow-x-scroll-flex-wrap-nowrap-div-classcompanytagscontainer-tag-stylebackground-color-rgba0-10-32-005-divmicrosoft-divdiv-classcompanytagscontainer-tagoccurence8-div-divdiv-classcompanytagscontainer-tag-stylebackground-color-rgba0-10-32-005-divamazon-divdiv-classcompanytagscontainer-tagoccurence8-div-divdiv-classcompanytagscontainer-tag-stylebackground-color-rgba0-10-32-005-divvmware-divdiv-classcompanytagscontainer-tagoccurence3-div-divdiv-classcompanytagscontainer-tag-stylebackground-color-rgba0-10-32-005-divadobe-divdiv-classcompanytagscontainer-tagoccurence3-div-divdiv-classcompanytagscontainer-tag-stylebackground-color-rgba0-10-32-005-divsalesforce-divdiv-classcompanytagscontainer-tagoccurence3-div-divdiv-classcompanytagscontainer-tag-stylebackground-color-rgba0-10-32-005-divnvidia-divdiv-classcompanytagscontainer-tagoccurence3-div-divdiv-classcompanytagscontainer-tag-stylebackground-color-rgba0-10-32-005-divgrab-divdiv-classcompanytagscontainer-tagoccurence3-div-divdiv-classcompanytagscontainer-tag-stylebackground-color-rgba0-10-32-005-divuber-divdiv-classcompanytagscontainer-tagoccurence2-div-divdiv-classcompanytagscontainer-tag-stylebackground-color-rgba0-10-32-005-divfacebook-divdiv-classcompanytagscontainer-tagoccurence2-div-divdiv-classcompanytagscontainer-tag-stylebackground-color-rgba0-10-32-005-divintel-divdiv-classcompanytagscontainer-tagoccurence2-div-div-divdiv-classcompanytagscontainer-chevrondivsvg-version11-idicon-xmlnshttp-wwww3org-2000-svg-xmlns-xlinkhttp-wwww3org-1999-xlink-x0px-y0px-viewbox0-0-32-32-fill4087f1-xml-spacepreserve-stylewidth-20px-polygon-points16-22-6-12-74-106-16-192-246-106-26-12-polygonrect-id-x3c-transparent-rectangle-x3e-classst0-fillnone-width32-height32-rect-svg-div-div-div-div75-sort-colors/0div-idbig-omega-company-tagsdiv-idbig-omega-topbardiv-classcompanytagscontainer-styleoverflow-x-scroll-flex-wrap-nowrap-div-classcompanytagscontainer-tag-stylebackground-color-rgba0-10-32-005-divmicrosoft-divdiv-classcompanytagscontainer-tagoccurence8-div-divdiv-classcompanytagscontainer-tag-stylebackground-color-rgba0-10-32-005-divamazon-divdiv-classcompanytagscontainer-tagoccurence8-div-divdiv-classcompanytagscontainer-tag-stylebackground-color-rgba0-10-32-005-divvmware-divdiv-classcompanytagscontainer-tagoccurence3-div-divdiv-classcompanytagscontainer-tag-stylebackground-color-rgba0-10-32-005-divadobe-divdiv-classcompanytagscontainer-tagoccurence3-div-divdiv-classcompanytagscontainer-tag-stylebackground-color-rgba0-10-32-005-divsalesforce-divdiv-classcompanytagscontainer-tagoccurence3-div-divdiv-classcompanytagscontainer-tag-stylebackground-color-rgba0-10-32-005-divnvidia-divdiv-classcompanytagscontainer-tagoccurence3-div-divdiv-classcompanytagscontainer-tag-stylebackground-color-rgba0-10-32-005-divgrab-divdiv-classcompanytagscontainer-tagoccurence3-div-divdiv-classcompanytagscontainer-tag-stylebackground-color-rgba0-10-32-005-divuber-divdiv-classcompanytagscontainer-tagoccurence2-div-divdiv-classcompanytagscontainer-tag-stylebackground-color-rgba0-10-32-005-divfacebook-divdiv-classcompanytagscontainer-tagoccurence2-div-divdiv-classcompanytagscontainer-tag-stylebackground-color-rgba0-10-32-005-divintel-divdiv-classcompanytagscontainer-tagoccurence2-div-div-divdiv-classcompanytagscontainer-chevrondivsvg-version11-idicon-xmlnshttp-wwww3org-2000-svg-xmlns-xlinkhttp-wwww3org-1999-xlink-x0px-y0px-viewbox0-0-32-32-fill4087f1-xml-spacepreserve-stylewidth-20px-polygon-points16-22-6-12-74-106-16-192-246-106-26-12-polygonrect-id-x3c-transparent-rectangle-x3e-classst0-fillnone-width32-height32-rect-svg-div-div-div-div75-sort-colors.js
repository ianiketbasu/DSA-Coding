/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let low = 0;
    let high = nums.length-1;
    let mid = 0;
    
    while(mid <= high){
        if(nums[mid] === 0){
            let temp = nums[mid];
            nums[mid++] = nums[low];
            nums[low++] = temp;
        }
        else if(nums[mid] === 1) mid++;
        else{
            let temp = nums[mid];
            nums[mid] = nums[high];
            nums[high--] = temp;
        }
    }
};