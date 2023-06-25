class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
#         num1 , num2 = 0 , 0
#         i , j = 0 , 0
#         while i < len(v1) and j < len(v2) :
#             if i==0 or v1[i] == '.':
#                 while v1[i] == '0' or v1[i] == '.':
#                     i += 1
#             if j==0 or v2[j] == '.':
#                 while v2[i] == '0' or v2[j] == '.':
#                     j += 1
#             num1 = num1*10 + int(v1[i])
#             i += 1
#             num2 = num2*10 + int(v2[j])
#             j += 1
        
#         print(num1,num2)
#         return 0

        # segment1 = [int(v) for v in v1.split('.')]
        # segment2 = [int(v) for v in v2.split('.')]
        # print(segment1,segment2)
        # num1 = int(''.join(str(num) for num in segment1))
        # num2 = int(''.join(str(num) for num in segment2))
        # print(num1,num2)
        # return -1 if num1 < num2 else 1 if num1 > num2 else 0
        segment1 = [int(v) for v in v1.split('.')]
        segment2 = [int(v) for v in v2.split('.')]

        # Ensure the segments have the same length
        while len(segment1) < len(segment2):
            segment1.append(0)
        while len(segment2) < len(segment1):
            segment2.append(0)

        for num1, num2 in zip(segment1, segment2):
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1

        return 0