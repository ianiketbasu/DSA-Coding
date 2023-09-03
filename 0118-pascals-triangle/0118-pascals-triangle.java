class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<>();
        
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>(i+1);
            
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i)
                    row.add(1);
                else{
                    int num1 = ans.get(i-1).get(j-1);
                    int num2 = ans.get(i-1).get(j);
                    row.add(num1+num2);
                }
            }
            
            ans.add(row);
        }
        
        return ans;
    }
}
