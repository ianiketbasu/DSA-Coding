class Solution {
    public double myPow(double x, int n) {      
        
        if(n == 0) return 1.0;
        double res = 1.0;
        long power = n;
        
        if(power < 0){
            x = 1 / x;
            power = -1*power;
        }
        
        while (power > 0) {
            if (power % 2 == 1) {
                res *= x;
            }
            x *= x;
            power /= 2;
        }
        
        return res;
    }
}