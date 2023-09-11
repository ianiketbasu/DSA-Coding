class Solution {
//     public List<List<Integer>> groupThePeople(int[] groupSizes) {
//         List<List<Integer>> result = new ArrayList<>();
//         HashMap<Integer, List<Integer>> map = new HashMap<>();

//         // Step 1: Group people by their group sizes
//         for (int i = 0; i < groupSizes.length; i++) {
//             int size = groupSizes[i];

//             // If the group size exists in the map, add the person's index to that group
//             if (map.containsKey(size)) {
//                 map.get(size).add(i);
//             } else {
//                 // If the group size doesn't exist, create a new group and add the person's index
//                 map.put(size, new ArrayList<>(Arrays.asList(i)));
//             }
//         }

//         // Step 2: Process each group in the map
//         for (Integer key : map.keySet()) {
//             List<Integer> group = map.get(key);

//             // If the group size matches the number of people in the group, add the whole group to the result
//             if (key == group.size()) {
//                 result.add(group);
//             } else {
//                 // If the group size is different, split the group into subgroups of the appropriate size
//                 for (int i = 0; i < group.size(); i += key) {
//                     result.add(group.subList(i, i + key));
//                 }
//             }
//         }

//         return result;
//     }
    
    
    public List<List<Integer>> groupThePeople(int[] gz) {
          List<List<Integer>> res = new ArrayList();
          Map<Integer, List<Integer>> groups = new HashMap<>();
          for (int i = 0; i < gz.length; ++i) {
            List<Integer> list = groups.computeIfAbsent(gz[i], expression -> new ArrayList());
            list.add(i);
            if (list.size() == gz[i]) {
              res.add(list);
              groups.put(gz[i], new ArrayList());
            }
          }
          return res;
    }
}
