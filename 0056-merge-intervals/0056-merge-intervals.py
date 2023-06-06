class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1 : return intervals
        intervals[:] = sorted(intervals)
        
        merged_li = [intervals[0]]
        
        for interval in intervals[1:] :
            if merged_li[-1][1] >= interval[0] : 
                merged_li[-1][1] = max(merged_li[-1][1],interval[1])
            else :
                merged_li.append(interval)
                
        return merged_li
                
            