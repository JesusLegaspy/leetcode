from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        newArr = []
        mdx = 0
        ndx = 0
        while(True):
          if(mdx >= m and ndx >= n):
            break
          if(mdx>= m):
            newArr.append(nums2[ndx])
            ndx = ndx + 1
            continue
          if(ndx>=n):
            newArr.append(nums1[mdx])
            mdx = mdx + 1
            continue
          if(mdx>= m  or nums2[ndx] < nums1[mdx]):
            newArr.append(nums2[ndx])
            ndx = ndx + 1
            continue
          if(ndx>=n or nums1[mdx] <= nums2[ndx]):
            newArr.append(nums1[mdx])
            mdx = mdx + 1
            continue
        
        for idx in range(len(nums1)):
          nums1[idx] = newArr[idx]

nums1 = [1]
m = 1
nums2 = []
n = 0
Solution().merge(nums1, m, nums2, n)
print(nums1)