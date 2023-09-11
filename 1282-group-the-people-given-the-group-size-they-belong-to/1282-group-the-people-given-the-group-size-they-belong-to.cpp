class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        vector<vector<int>> result;
        unordered_map<int, vector<int>> map;
        
        for (int i = 0; i < groupSizes.size(); i++) {
            int size = groupSizes[i];
            if (map.find(size) != map.end()) {
                map[size].push_back(i);
            } else {
                map[size] = {i};
            }
        }
        
        for (auto& kv : map) {
            vector<int>& group = kv.second;
            if (kv.first == group.size()) {
                result.push_back(group);
            } else {
                for (int i = 0; i < group.size(); i += kv.first) {
                    result.push_back(vector<int>(group.begin() + i, group.begin() + i + kv.first));
                }
            }
        }
        return result;
    }
};
