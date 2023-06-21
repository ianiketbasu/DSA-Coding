class Solution:
    def findMedianSortedArrays(self, array1: List[int], array2: List[int]) -> float:
        return sorted(array1 + array2)[len(array1 + array2) // 2] if len(array1 + array2) % 2 != 0 else (sorted(array1 + array2)[len(array1 + array2) // 2 - 1] + sorted(array1 + array2)[len(array1 + array2) // 2]) / 2