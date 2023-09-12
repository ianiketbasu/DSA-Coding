class Solution {
    public int trap(int[] height) {
        int n = height.length;
        if(n < 3) return 0;
        int[] lMaxArr = new int[n];
        int[] rMaxArr = new int[n];
        
        int lMaxVal = height[0]; // Initialize to the first element
        int rMaxVal = height[n - 1]; // Initialize to the last element
        
        for(int i=0;i<n;i++){
            lMaxVal = Math.max(lMaxVal,height[i]);
            lMaxArr[i] = lMaxVal;
            
            rMaxVal = Math.max(rMaxVal,height[n-i-1]);
            rMaxArr[n-i-1] = rMaxVal;
        }
        
        int water = 0;
        
        for(int i=1;i<n-1;i++){
            if(height[i] < lMaxArr[i] && height[i] < rMaxArr[i]){
                water += Math.min(lMaxArr[i],rMaxArr[i]) - height[i];
            }
        }
        
        return water;
    }
}


