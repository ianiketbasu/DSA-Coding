class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # ans = 0
        # counter = Counter()
        # for li in grid :
        #     counter[tuple(li)] += 1
        # grid[:] = zip(*grid[::1])
        # for tup in grid :
        #     if counter[tup] :
        #         ans += counter[tup]
        # return ans
      
        return sum([grid.count(list(col)) for col in list(zip(*grid))])