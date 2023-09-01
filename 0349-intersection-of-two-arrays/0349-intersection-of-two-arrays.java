class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashMap<Integer,Boolean> mp1 = new HashMap<>();
        HashMap<Integer,Boolean> mp2 = new HashMap<>();
        
        for(int num : nums1){
            mp1.put(num,true);
        }
        for(int num : nums2){
            mp2.put(num,true);
        }
        
        ArrayList<Integer> intersectionArray = new ArrayList<>();
        
        for(int num : mp1.keySet()){
            if(mp2.containsKey(num)){
                intersectionArray.add(num);
            }
        }
        
        int[] ans = new int[intersectionArray.size()];
        
        for(int i=0;i<intersectionArray.size();i++){
            ans[i] = intersectionArray.get(i);
        }
        
        return ans;
    }
}