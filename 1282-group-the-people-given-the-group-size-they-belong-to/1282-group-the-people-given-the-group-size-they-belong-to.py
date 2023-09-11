class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        groups = {}
        
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size in groups:
                groups[size].append(i)
            else:
                groups[size] = [i]
        
        for key, group in groups.items():
            if key == len(group):
                result.append(group)
            else:
                result.extend([group[i:i + key] for i in range(0, len(group), key)])
        
        return result
