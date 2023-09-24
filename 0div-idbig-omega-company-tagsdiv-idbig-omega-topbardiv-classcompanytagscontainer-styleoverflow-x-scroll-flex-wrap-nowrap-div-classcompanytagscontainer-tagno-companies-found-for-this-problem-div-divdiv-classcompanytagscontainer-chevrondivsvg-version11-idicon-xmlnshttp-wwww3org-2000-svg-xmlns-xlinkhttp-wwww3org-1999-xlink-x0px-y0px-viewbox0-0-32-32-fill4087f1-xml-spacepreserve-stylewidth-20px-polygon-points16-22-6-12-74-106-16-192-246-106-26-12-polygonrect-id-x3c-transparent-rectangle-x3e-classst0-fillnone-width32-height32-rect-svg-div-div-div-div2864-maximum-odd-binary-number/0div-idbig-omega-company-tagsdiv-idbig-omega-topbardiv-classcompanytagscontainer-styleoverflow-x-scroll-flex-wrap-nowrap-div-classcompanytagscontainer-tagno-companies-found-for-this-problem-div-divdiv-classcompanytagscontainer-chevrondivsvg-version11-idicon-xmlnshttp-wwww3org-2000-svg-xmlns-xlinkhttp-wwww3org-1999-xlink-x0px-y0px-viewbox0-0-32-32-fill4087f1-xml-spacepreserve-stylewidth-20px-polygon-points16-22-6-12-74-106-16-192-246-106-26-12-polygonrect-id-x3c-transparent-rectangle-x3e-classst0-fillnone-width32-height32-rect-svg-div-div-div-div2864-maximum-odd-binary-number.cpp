class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int n = s.length();
        int count_one = 0;
        
        for(char ch : s) 
            if(ch == '1') 
                count_one++;
        
        int count_zero = n - count_one;

        
        
//         String ans = "";
//         for(int i=0;i<count_one - 1;i++) ans += "1";
//         for(int i=0;i<count_zero;i++) ans += "0";
//         if(count_one > 0) ans += "1";
        
//         return ans;
        
        for(int i = 0; i < count_one - 1;i++) s[i] = '1';
        for(int i = count_one - 1;i < n - 1 ; i++) s[i] = '0';
        s[n-1] =  '1';
        
        return s;
    }
};