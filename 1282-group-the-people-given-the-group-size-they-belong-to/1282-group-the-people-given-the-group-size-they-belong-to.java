class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        List<List<Integer>> result = new ArrayList<>();
        HashMap<Integer,List<Integer>> map = new HashMap<>();
        
        for(int i=0;i<groupSizes.length;i++){
            int size = groupSizes[i];
            if(map.get(size) != null){
                map.get(size).add(i);
            }
            else map.put(size , new ArrayList<>(Arrays.asList(i)));
        }
        
        for(Integer key : map.keySet()){
            List<Integer> group = map.get(key);
            if(key == group.size())
                result.add(group);
            else{
                for(int i=0;i<group.size();i+=key){
                    result.add(group.subList(i,i+key));
                }
            }
        }
        return result;
    }
}