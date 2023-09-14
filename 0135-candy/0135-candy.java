class Solution {
    public int candy(int[] ratings) {
        int len = ratings.length;
        int[] candyArr = new int[len];
        
        Arrays.fill(candyArr,1);
        
        for(int i=1;i<len;i++){
            if(ratings[i] > ratings[i-1]){
                candyArr[i] = candyArr[i-1] + 1;
            }
        } 
        
        
        for(int i=len-2;i>-1;i--){
            if(ratings[i] > ratings[i+1] && candyArr[i] <= candyArr[i+1]){
                candyArr[i] = candyArr[i+1] + 1;
            }
        }

        
        int totalCandy = 0;
        for(int candy : candyArr){
            totalCandy += candy;
        }
        
        return totalCandy;
    }
}