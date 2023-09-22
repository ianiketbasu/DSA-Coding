class Solution {
    public int findKthLargest(int[] nums, int k) {
        // Arrays.sort(nums);
        // return nums[nums.length - k];
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int num : nums){
            if(pq.size() < k) pq.add(num);
            else if(pq.peek() < num){
                pq.remove();
                pq.add(num);
            }
        }
        
        return pq.peek();
    }
}