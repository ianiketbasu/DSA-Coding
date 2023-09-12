class Solution {
    public int minDeletions(String s) {
        int[] freq = new int[26];
        Set<Integer> set = new HashSet<>();
        int ans = 0;
        
        for(int i=0;i<s.length();i++){
            Character c = s.charAt(i);
            freq[c - 'a']++;
        }
        
        for(int i=0;i<26;i++){
            while(freq[i] > 0 && !set.add(freq[i])){
                ans++;
                freq[i]--;
            }
        }
        return ans;
    }
}