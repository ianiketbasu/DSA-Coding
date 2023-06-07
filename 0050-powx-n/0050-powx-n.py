class Solution:
    def myPow(self, x: float, n: int) -> float:
#         isNegative = False
#         if n < 0 : 
#             isNegative = True
#         ans = 1.0
#         n = abs(n)
#         for i in range(0,n) :
#             ans *= x
        
#         if isNegative :
#             return 1 / ans
        
#         return ans


            ans = 1.0
            flg = n < 0
            n = abs(n)
            while n > 0 :
                if n%2 == 1 :
                    ans *= x
                x *= x
                n //= 2
                
            return 1 / ans if flg else ans