class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder ans = new StringBuilder();
        for(int i=0;i<words.length;i++){
            String word = words[i];
            StringBuilder reversed = new StringBuilder();
            for(int j=word.length() - 1 ; j >= 0 ; j--){
                reversed.append(word.charAt(j));
            }
            ans.append(reversed);
            if(i != words.length - 1)
                ans.append(" ");
            
        }
        return ans.toString();
    }
}