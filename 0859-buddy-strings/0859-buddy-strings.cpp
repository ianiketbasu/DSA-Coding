// class Solution {
// public:
//     bool buddyStrings(string s, string goal) {
//         int n1 = s.size();
//         int n2 = goal.size();
//         // set<char>st;
//         if(n1 != n2) return false;
//         int idx1 , idx2 , i;
//         for(i = 0 ; i < n1 ; i++){
//             if(s[i] != goal[i]){
//                 idx1 = i;
//                 break;
//             }
//         }
//         // cout<<i<<endl;
//         if(i == n1) {
//             // for(int j=0 ; j<n1 ; j++) st.insert(s[j]);
//             // if(st.size() == n1) return false;
//             // return true;
//             set<char> st(s.begin() , s.end());
//             return st.size() < n1;
            
//         }
//         i++;
//         for( ; i < n1 ; i++){
//             if(s[i] != goal[i]){
//                 idx2 = i;
//                 break;
//             }
//         }
//         // cout<<i;
//         swap(goal[idx1],goal[idx2]);
//         if(s.compare(goal) == 0) return true;
//         return false;
        
//     }
// };


class Solution {
public:
    bool buddyStrings(string s, string g) {
        if(s == g){
            set<char> st(s.begin(),s.end());
            return st.size() < s.size();
        }
        
        int low = 0 , high = s.size() - 1;
        
        while(low < s.size() and s[low] == g[low]) low++;
        
        while(high >= 0 and s[high] == g[high]) {
            high--;
        }
        
        if(low < high) swap(s[low],s[high]);
        
        return s == g;
    }
};