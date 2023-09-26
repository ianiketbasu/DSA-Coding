class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> map = new HashMap<>();
        
        for(int num : nums) {
            map.put(num , map.getOrDefault(num,0) + 1);
        }
        
        PriorityQueue<Pair<Integer,Integer>> pq = new PriorityQueue<>(
            (a,b) -> b.getKey() - a.getKey()
        );
        
        for(Map.Entry<Integer,Integer> entry : map.entrySet()){
            pq.offer(new Pair<>(entry.getValue() , entry.getKey()));
        }
        
        ArrayList<Integer> list = new ArrayList<>();
        while(k != 0){
            list.add(pq.poll().getValue());
            k--;
        }
        
        int[] ans = new int[list.size()];
        
        for(int i=0;i<list.size();i++) {
            ans[i] = list.get(i);
        }
        
        return ans;
        
        
    }
}