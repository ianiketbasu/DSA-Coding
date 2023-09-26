class Solution {
    public String removeDuplicateLetters(String s) {
        int[] freq = new int[26];
        int[] visited = new int[26];
        
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }
        
        StringBuilder sb = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            freq[c - 'a']--;
            
            if (visited[c - 'a'] == 0) {
                while (sb.length() > 0 && c < sb.charAt(sb.length() - 1) && 
                       freq[sb.charAt(sb.length() - 1) - 'a'] > 0) {
                    
                    visited[sb.charAt(sb.length() - 1) - 'a'] = 0;
                    sb.deleteCharAt(sb.length() - 1);
                    
                }
                sb.append(c);
                visited[c - 'a'] = 1;
            }
        }
        
        return sb.toString();
    }
}
