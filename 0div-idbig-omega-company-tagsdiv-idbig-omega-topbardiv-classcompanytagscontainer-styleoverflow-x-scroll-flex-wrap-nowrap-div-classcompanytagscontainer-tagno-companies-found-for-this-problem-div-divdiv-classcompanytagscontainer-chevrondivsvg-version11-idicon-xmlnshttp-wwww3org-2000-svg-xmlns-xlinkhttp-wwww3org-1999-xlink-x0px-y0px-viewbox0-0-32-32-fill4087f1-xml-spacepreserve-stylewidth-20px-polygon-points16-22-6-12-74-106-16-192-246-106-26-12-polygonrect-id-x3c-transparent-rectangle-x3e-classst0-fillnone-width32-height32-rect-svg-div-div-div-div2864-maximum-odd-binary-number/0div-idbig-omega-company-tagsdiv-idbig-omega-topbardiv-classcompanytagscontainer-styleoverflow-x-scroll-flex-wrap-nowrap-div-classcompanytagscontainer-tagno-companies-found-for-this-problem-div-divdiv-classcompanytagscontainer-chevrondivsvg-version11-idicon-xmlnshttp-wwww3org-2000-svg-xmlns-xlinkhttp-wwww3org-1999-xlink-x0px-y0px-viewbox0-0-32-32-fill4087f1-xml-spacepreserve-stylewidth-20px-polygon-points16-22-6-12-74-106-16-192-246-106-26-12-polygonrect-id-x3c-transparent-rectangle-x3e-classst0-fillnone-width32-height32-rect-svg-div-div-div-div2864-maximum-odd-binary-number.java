class Solution {
    public String maximumOddBinaryNumber(String s) {
        int count_one = 0;
        int count_zero = 0;
        
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) == '1') count_one++;
            else count_zero++;
        }
        
        String ans = "";
        for(int i=0;i<count_one - 1;i++) ans += "1";
        for(int i=0;i<count_zero;i++) ans += "0";
        if(count_one > 0) ans += "1";
        
        return ans;
    }
}