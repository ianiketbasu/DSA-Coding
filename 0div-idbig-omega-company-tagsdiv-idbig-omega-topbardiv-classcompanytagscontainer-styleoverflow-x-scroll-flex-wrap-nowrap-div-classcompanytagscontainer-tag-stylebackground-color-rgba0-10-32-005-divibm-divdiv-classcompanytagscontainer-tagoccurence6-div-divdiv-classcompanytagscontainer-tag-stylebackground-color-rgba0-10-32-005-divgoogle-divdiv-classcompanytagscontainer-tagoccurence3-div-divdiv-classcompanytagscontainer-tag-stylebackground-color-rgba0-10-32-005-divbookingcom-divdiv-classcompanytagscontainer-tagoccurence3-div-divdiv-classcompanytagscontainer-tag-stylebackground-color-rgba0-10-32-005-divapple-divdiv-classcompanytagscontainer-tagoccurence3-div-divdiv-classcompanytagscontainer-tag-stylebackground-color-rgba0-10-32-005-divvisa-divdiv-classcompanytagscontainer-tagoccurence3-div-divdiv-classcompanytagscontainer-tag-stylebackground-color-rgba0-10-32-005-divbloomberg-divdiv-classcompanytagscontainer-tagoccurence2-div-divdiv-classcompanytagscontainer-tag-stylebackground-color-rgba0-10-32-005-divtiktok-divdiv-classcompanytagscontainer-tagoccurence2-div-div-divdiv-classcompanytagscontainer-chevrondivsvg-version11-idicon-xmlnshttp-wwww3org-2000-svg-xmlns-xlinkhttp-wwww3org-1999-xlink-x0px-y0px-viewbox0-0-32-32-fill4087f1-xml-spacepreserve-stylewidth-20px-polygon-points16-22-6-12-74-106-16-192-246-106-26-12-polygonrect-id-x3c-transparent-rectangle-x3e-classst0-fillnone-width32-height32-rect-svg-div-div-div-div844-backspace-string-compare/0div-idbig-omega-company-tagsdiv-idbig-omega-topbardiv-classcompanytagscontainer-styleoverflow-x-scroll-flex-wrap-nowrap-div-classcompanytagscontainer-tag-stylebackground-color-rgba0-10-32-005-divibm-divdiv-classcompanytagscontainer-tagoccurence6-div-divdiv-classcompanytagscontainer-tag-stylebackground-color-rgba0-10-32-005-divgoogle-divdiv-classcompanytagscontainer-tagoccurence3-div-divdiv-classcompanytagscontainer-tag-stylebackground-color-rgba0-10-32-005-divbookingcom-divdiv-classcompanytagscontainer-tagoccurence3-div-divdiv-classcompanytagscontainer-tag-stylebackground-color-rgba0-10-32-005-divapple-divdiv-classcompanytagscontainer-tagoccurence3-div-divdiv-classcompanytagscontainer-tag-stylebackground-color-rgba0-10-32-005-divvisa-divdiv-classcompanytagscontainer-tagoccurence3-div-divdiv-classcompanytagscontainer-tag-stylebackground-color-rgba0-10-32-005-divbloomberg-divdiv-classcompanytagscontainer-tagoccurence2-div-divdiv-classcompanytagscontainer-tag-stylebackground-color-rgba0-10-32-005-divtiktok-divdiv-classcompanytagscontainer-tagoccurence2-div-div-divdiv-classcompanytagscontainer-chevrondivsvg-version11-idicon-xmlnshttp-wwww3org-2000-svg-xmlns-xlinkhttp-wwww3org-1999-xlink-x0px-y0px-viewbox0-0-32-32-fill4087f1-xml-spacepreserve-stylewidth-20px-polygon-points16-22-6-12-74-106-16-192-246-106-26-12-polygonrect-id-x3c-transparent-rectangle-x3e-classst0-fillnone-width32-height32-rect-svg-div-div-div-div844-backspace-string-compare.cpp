class Solution {
    string stringFilter(string &s){
        string st = "";
        int count = 0;
        for(int i = s.size() - 1 ; i >= 0 ; i--){
            
            if(s[i] == '#') count++;
            else{
                if(count > 0) count--;
                else st = s[i] + st;
            }
        }
        
        return st;
    }
public:
    bool backspaceCompare(string s, string t) {
        /* wrong code */
//         int i=s.size()-1 , j=t.size()-1;
//         while(i>=0 or j>=0){
            
//             if(s[i] == '#'){
//                 int count = 0;
//                 while(s[i] == '#') {
//                     count++;
//                     i--;
//                 }
//                 i = i - count;
                
//             }
//             if(t[j] == '#'){
//                 int count = 0;
//                 while(t[j] == '#') {
//                     count++;
//                     j--;
//                 }
//                 j = j - count;
//             }
//             if(i<0 and j<0) return true;
//             else if(i>=0 and j<0) return false;
//             else if(i<0 and j>=0) return false;
//             if(t[j] == s[i]){
//                 i--;
//                 j--;
//             }else return false;
            
//         }
        
//         return true;
        
//         string r1 = "" , r2 = "";
//         int i=0;
        
//         while(s[i] != '\0'){
//             if(s[i] != '#') r1 += s[i];
//             else if(!r1.empty()) r1.pop_back();
//             i++;
//         }
        
//         i = 0;
//         while(t[i] != '\0'){
//             if(t[i] != '#') r2 += t[i];
//             else if(!r2.empty()) r2.pop_back();
//             i++;
//         }
        
//         if(r1.compare(r2) == 0) return true;
//         return false;
        
        
//         int sback=0,tback=0;
//         int i=s.length()-1,j=t.length()-1;
//         char hash='#';
        
//         while(i>=0 || j>=0)
//         {
//             //find first non # character in s string
//             while(i>=0)
//             {
//                 if(s[i]==hash)
//                 {
//                     sback++;
//                     i--;
//                 }
//                 else if(sback>0)
//                 {
//                     sback--;
//                     i--;
//                 }
//                 else
//                     break;
//             }
            
//             //find first non # character in t string
//             while(j>=0)
//             {
//                 if(t[j]==hash)
//                 {
//                     tback++;
//                     j--;
//                 }
//                 else if (tback>0)
//                 {
//                     tback--;
//                     j--;
//                 }
//                 else
//                     break;
//             }
            
//             if(i>=0 && j>=0 && s[i]!=t[j])
//                 return false;
//             if((i>=0) != (j>=0))
//                 return false;
            
//             i--;
//             j--;
//         }
        
//         return true;
    
       
        return stringFilter(s) == stringFilter(t);
        
        
        
         
       
    }
    
};