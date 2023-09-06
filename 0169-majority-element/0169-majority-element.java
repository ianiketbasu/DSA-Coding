import java.util.Map.Entry;
class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> myMap = new HashMap<>();
        int len = nums.length;
        for(Integer num : nums){
            if(myMap.containsKey(num)){
                myMap.put(num,myMap.get(num) + 1);
            }
            else{
                myMap.put(num,1);
            }
        }
        for(Entry<Integer,Integer> entry : myMap.entrySet()){
            if(entry.getValue() > len/2) return entry.getKey();
        }
        return 0;
    }
}