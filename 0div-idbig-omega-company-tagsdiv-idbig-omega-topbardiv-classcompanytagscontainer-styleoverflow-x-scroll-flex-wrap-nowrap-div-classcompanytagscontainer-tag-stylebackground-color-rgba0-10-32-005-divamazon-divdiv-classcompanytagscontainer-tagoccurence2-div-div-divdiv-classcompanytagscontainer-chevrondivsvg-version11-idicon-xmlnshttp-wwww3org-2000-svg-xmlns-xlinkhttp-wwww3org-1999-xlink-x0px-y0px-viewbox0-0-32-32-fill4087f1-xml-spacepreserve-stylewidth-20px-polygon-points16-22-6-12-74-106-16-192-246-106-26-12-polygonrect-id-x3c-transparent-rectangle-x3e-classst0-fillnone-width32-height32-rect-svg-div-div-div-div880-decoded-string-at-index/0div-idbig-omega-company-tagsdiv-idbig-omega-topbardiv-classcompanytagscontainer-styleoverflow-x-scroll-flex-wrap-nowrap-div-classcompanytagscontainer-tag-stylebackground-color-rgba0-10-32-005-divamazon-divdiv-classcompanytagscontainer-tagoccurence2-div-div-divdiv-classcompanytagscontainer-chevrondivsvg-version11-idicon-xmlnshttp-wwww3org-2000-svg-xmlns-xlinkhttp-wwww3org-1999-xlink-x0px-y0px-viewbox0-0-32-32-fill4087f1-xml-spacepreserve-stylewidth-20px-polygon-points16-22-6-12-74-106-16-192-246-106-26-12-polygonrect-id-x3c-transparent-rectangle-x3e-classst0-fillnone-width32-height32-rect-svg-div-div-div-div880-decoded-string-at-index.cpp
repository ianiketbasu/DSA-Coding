class Solution {
public:
    string decodeAtIndex(string s, int k) {
        long long len=0;
        //Calculating Total length of decoded string
        for(auto i:s){
            if(isdigit(i)){
                len*=i-'0';
            }else{
                len++;
            }
        }

        //Traverse to find kth char in string
        for(int i=s.size()-1;i>=0;i--){
            if(isdigit(s[i])){
                len/=s[i]-'0';//To reemove repeated part in decoded string
                k%=len;//Adjusting k as per len of decoded string
            }else{
                if(k==0 or len==k){
                    return string("")+s[i];
                }
                len--;
            }
        }
        return "";
    }
};