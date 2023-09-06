// import java.util.Map.Entry;
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer,Integer> myMap = new HashMap<>();
        
        for(Integer num : nums){
            if(myMap.containsKey(num)){
                myMap.replace(num,myMap.get(num) + 1);
            }
            else{
                myMap.put(num,1);
            }
        }
        
        List<Integer> ans = new ArrayList<>();
        
        // for(Entry<Integer,Integer> entry : myMap.entrySet()){
        //     if(entry.getValue() > (nums.length / 3)){
        //         ans.add(entry.getKey());
        //     }
        // }
        
        for(Integer key : myMap.keySet()){
            if(myMap.get(key) > nums.length/3){
                ans.add(key);
            }
        }
        
        return ans;
    }
}