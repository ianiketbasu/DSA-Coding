// class Solution {
//     public int candy(int[] ratings) {
//         int ans = 0;
//         int len = ratings.length;
//         for(int i=0;i<len;++i){
//             int prev_assign_value = 0;
//             if(i == 0){
//                 if(i + 1 < len){
//                     if(ratings[i] <= ratings[i+1]){
                        
//                     }
//                 }
//                 else return 1;
//             }else if(i == len -1){
                
//             }else{
                
//             }
//         }
//         return ans;
//     }
// }

class Solution {
    public int candy(int[] ratings) {
        int len = ratings.length;
        int[] candies = new int[len];
        Arrays.fill(candies, 1); // Initialize candies with all 1s
        
        // Scan left to right
        for (int i = 1; i < len; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        
        // Scan right to left
        for (int i = len - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1]) {
                candies[i] = candies[i + 1] + 1;
            }
        }
        
        int totalCandies = 0;
        for (int candyCount : candies) {
            totalCandies += candyCount;
        }
        
        return totalCandies;
    }
}
