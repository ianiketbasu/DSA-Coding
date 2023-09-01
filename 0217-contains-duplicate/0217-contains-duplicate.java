class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer,Integer> mymap = new HashMap<>();
        
        for(int num : nums){
            if(mymap.containsKey(num)){
                mymap.put(num,mymap.get(num)+1);
            }
            else{
                mymap.put(num,1);
            }
        }
        
        for(Map.Entry<Integer,Integer> entry : mymap.entrySet()){
            if(entry.getValue() > 1){
                return true;
            }
        }
        
        return false;
    }
}