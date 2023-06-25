class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        
        segment1 = [int(v) for v in v1.split('.')]
        segment2 = [int(v) for v in v2.split('.')]

        # Ensure the segments have the same length
        while len(segment1) < len(segment2):
            segment1.append(0)
        while len(segment2) < len(segment1):
            segment2.append(0)
        print(segment1,segment2)
        for num1, num2 in zip(segment1, segment2):
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1

        return 0