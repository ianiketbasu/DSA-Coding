class Solution {
public:
    bool isAnagram(string s, string t) {
        
        //boundary case . . .
	    if(s.size() != t.size()) return false;
    
        unordered_map<char,int> mymap;
    
	    //you can use for loop or iterator also . . .
        // for(int i=0;i<s.size();i++) mymap[s[i]]++;
        // for(int i=0;i<t.size();i++) mymap[t[i]]--;
	    
        for(auto i : s) mymap[i]++;
        for(auto i : t) mymap[i]--;
    
        for(auto i : mymap) if(i.second != 0) return false;
    
        return true;
    }
};