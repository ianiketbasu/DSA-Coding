class Solution {
public:
    string largestOddNumber(string num) {
        // int n = size(num);
        // for(int i=n-1;i>=0;i--) if((num[i]-'0')%2 != 0) return num.substr(0,i+1);
        // return "";
        
        // return num.substr(0, num.find_last_of("13579") + 1);  
        return num.substr(0, num.find_last_of("1|3|5|7|9") + 1);  
        // return num.substr(0, num.find_last_not_of("02468") + 1);
        // return num.substr(0, num.find_last_not_of("0|2|4|6|8") + 1);
    }
};