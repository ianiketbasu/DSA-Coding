class Solution {
public:
    string reverseWords(string s) {
        istringstream iss(s);
        string word;
        vector<string> words;
        while(iss>>word){
            words.push_back(word);
        }
        
        string res = "";
        for(int i=words.size()-1;i>-1;i--){
            res += words[i];
            if(i != 0) res += " ";
        }
        
        return res;
        
    }
};