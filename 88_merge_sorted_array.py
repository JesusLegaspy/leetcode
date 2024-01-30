from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for idx in range(len(nums1)-1, -1, -1):
            if not (m != 0 and n==0) and ((m == 0 and n != 0) or nums1[m-1] < nums2[n-1]):
                nums1[idx] = nums2[n-1]
                n = n -1
            else:
                nums1[idx] = nums1[m-1]
                m = m - 1


       

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1]
m = 1
nums2 = []
n = 0
Solution().merge(nums1, m, nums2, n)
print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
Solution().merge(nums1, m, nums2, n)
print(nums1)