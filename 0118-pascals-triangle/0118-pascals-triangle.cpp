class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if n == 1 :
            return [[1]]
        elif n == 2 :
            return [[1],[1,1]]
        elif n == 3 :
            return [[1],[1,1],[1,2,1]]
        
        
        li = [[1],[1,1],[1,2,1]]
        
        for i in range(4,n+1) :
            temp_li = [1]
            last_li = li[len(li) - 1]
            for j in range(1,len(last_li)) :
                sum_ = last_li[j] + last_li[j-1]
                temp_li.append(sum_)
            temp_li.append(1)
            li.append(temp_li)
        
        return li