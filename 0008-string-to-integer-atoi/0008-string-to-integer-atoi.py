class Solution:
    def myAtoi(self, s: str) -> int:
        result , sign , n , i = 0 , 1 , len(s) , 0
        if n == 0 : return 0
        while i < n and s[i] == ' ' :
            i+=1
        
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        while i < n :
            if not s[i].isdigit() :
                break
            
            digit = int(s[i])
            result = result*10 + digit
            print(result)
            if result*sign < -2**31:
                return -2**31
            elif result*sign > (2**31 - 1):
                return (2**31 - 1) 
            i+=1
        
        return result * sign