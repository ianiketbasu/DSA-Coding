// import java.util.Map.Entry;
class Solution {
    public List<Integer> majorityElement(int[] nums) {
//         HashMap<Integer,Integer> myMap = new HashMap<>();
        
//         for(Integer num : nums){
//             if(myMap.containsKey(num)){
//                 myMap.replace(num,myMap.get(num) + 1);
//             }
//             else{
//                 myMap.put(num,1);
//             }
//         }
        
//         List<Integer> ans = new ArrayList<>();
        
//         // for(Entry<Integer,Integer> entry : myMap.entrySet()){
//         //     if(entry.getValue() > (nums.length / 3)){
//         //         ans.add(entry.getKey());
//         //     }
//         // }
        
//         for(Integer key : myMap.keySet()){
//             if(myMap.get(key) > nums.length/3){
//                 ans.add(key);
//             }
//         }
        
//         return ans;
        
        int count1 = 0 , count2 = 0;
        int ele1 = Integer.MAX_VALUE , ele2 = Integer.MAX_VALUE;
        
        for(int num : nums){
            if(count1 == 0 && ele2 != num){
                ele1 = num;
                count1++;
            }
            else if(count2 == 0 && ele1 != num){
                ele2 = num;
                count2++;
            }
            else if(num == ele1) count1++;
            else if(num == ele2) count2++;
            else{
                count1--;
                count2--;
            }
        }
        // System.out.println(ele1 + " " +count1 + " "+ ele2 + " " + count2);
        
        count1 = 0 ;
        count2 = 0;
        for(int num : nums){
            if(num == ele1) count1++;
            else if(num == ele2) count2++;
        }
        
        List<Integer> ans = new ArrayList<>();
        if(count1 > nums.length/3) ans.add(ele1);
        if(count2 > nums.length/3) ans.add(ele2);
        
        return ans;
        
    }
}