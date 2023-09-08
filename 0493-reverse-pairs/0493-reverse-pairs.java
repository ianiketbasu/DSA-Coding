class Solution {
    public int merge(int[] nums,int low,int mid,int high){
        int[] temp = new int[high - low + 1];
        int count = 0 , left = low , right = mid + 1 , index = 0;
        int leftPointer = low , rightPointer = mid + 1;
        
        while(leftPointer <= mid && rightPointer <= high){
            if((long)nums[leftPointer] > (long)2*nums[rightPointer]){
                count += (mid - leftPointer + 1);
                rightPointer++;
            }
            else{
                leftPointer++;
            }
        }
        
        while(left <= mid && right <= high){
            if(nums[left] > nums[right]){
                temp[index++] = nums[right++];
            }
            else{
                temp[index++] = nums[left++];
            }
        }
        
        while(left <= mid ){
                temp[index++] = nums[left++];   
        }
        
        while(right <= high){
                temp[index++] = nums[right++];
        }
        
        for(int i=0;i<high-low+1;i++){
            nums[low+i] = temp[i];
        }
        return count;
    }
    

    public int mergeSort(int[] nums,int low,int high){
        int count = 0;
        if(low >= high) return 0;
        int mid = (low+high) / 2;
        
            
        count += mergeSort(nums,low,mid) + mergeSort(nums,mid+1,high);
            
        count += merge(nums,low,mid,high);

        return count;
    }
    
    
    public int reversePairs(int[] nums) {
        return mergeSort(nums,0,nums.length-1);
    }
}