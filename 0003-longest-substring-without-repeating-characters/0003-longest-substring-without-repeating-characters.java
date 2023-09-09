class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        if(n == 0) return 0;
        int max_len = 1;
//         Set<Character> set = new HashSet<>();
//         int left = 0, right = 0;
        
//         while(right < n){
//             while(left < n && set.contains(s.charAt(right))){
//                 set.remove(s.charAt(left));
//                 left++;
//             }
//             set.add(s.charAt(right));
//             max_len = Math.max(max_len,right - left + 1);
//             right++;
//         }        
//         return max_len;
        
        Map<Character,Integer> map = new HashMap<>();
        int left = 0 , right = 0;
        
        while(right < n){
            if(map.get(s.charAt(right)) != null)
                left = Math.max((map.get(s.charAt(right)) + 1) , left);

            map.put(s.charAt(right),right);
            max_len = Math.max(max_len,right - left + 1);
            right++;
        }
        return max_len;
    }
}

