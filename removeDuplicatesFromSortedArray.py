class Solution:
    def removeDuplicates(self, nums):
      nums[:] = sorted(list(set(nums)))
      return len(nums)


myList = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(myList))
print(myList)